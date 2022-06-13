# Baseball system

## Introduction
Provide an website that you can subscribe and search for the score.

Aslo can update the score on the terminal.
## Tool
 * Python
    * flask
    * kazoo(Zookeeper)
    * requests
## Install
After clon
1. set up zookeeper-modify the path of dataDir and dataLogDir in each zookeeper/sever1 sever2 sever3/conf/zoo.cfg
2. ```./zkServer.sh start``` in each zookeeper/sever1 sever2 sever3/bin (mac)
3. run ```pip3 install -r packet.txt``` in code file
4. run ```python3 Stadium.py```
5. open another terminal to run ```python3 main.py```, than it create a url that you can connect to the webset you can use search and subscribe service on it
6. If you want to update the score, type the correct format in terminal which is running Stadium.py

If you don't know how to work, you can see the demo video on the youtube!

https://www.youtube.com/watch?v=uo9i0d-kM6M
