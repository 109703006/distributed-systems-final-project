from kazoo.client import KazooClient
zk = KazooClient(hosts='127.0.0.1') #如果是本地那就寫127.0.0.1
zk.start() #與zookeeper連接
stat=zk.get('/a')
print(stat)
stat=zk.get('/')
print(stat)
zk.stop()    #与zookeeper断开
