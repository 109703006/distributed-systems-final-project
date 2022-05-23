from kazoo.client import *

zk = KazooClient()
zk.start()
children = zk.get_children('/')
zk.stop()