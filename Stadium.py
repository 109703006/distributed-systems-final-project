from kazoo.client import *
import argparse

HINT_MSG = (
    "Please format your input as: Stadium, Date, Team, Score\n"
    "Type q to cancel the connection\n"
    ">>> "
)

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="IP address of zooKeeper server, default using localhost")
args = parser.parse_args()

IP = 'localhost'
if args.server:
    IP = args.server
server_list = []
for i in range(3):
    server_list.append(IP + ':' + str(2181+i))

# print(server_list)

zk = KazooClient(IP)
zk.start()
cmd = input(HINT_MSG)
while cmd != 'q':
    data = cmd.split(' ')
    # print(data)
    if len(data) == 4:
        path = '/' + data[0] + '/' + data[1]
        data = data[2] + ':' + data[3]
        data = data.encode("utf-8")
        zk.create(path, data, makepath=True)
    cmd = input(HINT_MSG)
zk.stop()