from kazoo.client import *
import argparse

# The input should avoid using / since it would be seen as next level of directory
HINT_MSG = (
    "Please format your input as: Stadium Month-Day Team1:Team2 Score1:Score2\n"
    "Type q to cancel the connection\n"
    ">>> "
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--server", help="IP address of zooKeeper server, default using localhost"
)
args = parser.parse_args()

# IP = 'localhost'
# if args.server:
#     IP = args.server
# # Assume the same IP address with port 2181~2183
# server_list = IP + ':' + str(2181)
# for i in range(1,3):
#     server_list += (',' + IP + ':' + str(2181+i))
# # print(server_list)
server_list = "192.168.56.101,192.168.56.102,192.168.56.103"

zk = KazooClient(server_list)
zk.start()

cmd = input(HINT_MSG)
while cmd != "q":
    data = cmd.split(" ")
    # print(data)
    if len(data) == 4:
        path = "/" + data[0] + "/" + data[1]
        data = data[2] + "=" + data[3]
        data = data.encode("utf-8")
        zk.create(path, data, makepath=True)
    cmd = input(HINT_MSG)
zk.stop()
