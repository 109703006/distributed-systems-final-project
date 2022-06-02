from kazoo.client import *

class Fans():
    def __init__(self, host='localhost'):
        server_list = host + ':' + str(2181)
        for i in range(1,3):
            server_list += (',' + host + ':' + str(2181+i))
        self.zk = KazooClient(server_list)
        self.zk.start()
    def close(self):
        self.zk.close()
    def getStadium(self):
        return self.zk.get_children('/')
    def subscribe(self, path):
        @self.zk.ChildrenWatch(path) # DataWatch 
        def watch_children(children): # data state
            print(children)


# For Test Only
# Me = Fans()
# str = input()
# while str != 'q':
#     if str == 'ls':
#         print(Me.getStadium())
#     else:
#         path = str.split()[1]
#         Me.subscribe(path)
#     str = input()
