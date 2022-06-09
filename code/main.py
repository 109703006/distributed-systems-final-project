from flask import Flask,request,redirect,url_for,render_template
from flask_socketio import SocketIO, emit
import configs
# 
# 最終版中要刪除
import codecs
# 

app = Flask(__name__, static_folder="static", static_url_path="/")
app.config.from_object(configs)
socketio = SocketIO(app,logger=True)
flag=False


'''
訂閱功能需要kazoo client, 所以下方跟Stadium.py 一樣建立一個kazoo client, 連到的kazoo server ip addresses 相同
'''
from kazoo.client import *
IP = "localhost"
# Assume the same IP address with port 2181~2183
server_list = IP + ":" + str(2181)
for i in range(1, 3):
    server_list += "," + IP + ":" + str(2181 + i)

zk = KazooClient(server_list)
zk.start()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    place=request.form['Stadium']
    time=request.form['Time']
    allInfo="目前沒有比賽\n"

    path = "./code/info.txt"

    file_ = codecs.open(path, "r", encoding="utf-8")
    lines = file_.readlines()
    file_.close()

    i = 0
    for cmd in lines:
        cmd = cmd.replace("\r\n", "")
        data = cmd.split(" ")
        print(data)
        if data[0]==place and data[1]==time:
            i+=1
            allInfo = allInfo.replace("目前沒有比賽", "")
            allInfo+=str(i)+"."+data[2]+" "+data[3]+"\n"
            print(allInfo)

    print("search:",place,time,allInfo)
    return render_template("index.html", result="Result: ", score=allInfo)
    
@app.route("/subscribe", methods=['POST'])
def subscribe():
    place=request.form['Stadium']
    print("subscribe:",place)
    
    # 用節點方式紀錄目前有訂閱的球場
    if not zk.exists(f"/subscription/{place}"):
        zk.create(f"/subscription/{place}", makepath=True)

    return render_template("index.html")

@socketio.on('subscribe')
def push():
    global flag
    flag=False
    while (True):
        socketio.sleep(1)

        '''
        以下的loop目前是回傳所有有訂閱的球場的"所有比賽資訊"，目前尚未跟Stadium.py的DataWatch function合併一起，目前尚卡在技術問題
        '''

        subscribedStadiums = zk.get_children(f"/subscription")
        for i, stadium in enumerate(subscribedStadiums):
            print(f"stadium : {stadium}")
            #針對每個訂閱的球場，找出所有節點
            allDates = zk.get_children(f"/{stadium}")
            for j, date in enumerate(allDates):
                print(f"stadium : {stadium}, date : {date}")
                #讀取該日期(也就是node)的value
                data, stat = zk.get(f"/{stadium}/{date}")
                socketio.send(f"stadium : {stadium}, date : {date}" + data.decode("utf-8"))

        if(flag):
            break
    
@socketio.on('stop')
def stop():
    global flag
    flag=True
    socketio.send("stop")
    
if __name__ == "__main__":
    socketio.run(app)
