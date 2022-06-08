from cv2 import line
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
    return render_template("index.html")

@socketio.on('subscribe')
def push():
    global flag
    flag=False
    while (True):
        socketio.sleep(1)
        socketio.send("test")
        if(flag):
            break
    
@socketio.on('stop')
def stop():
    global flag
    flag=True
    socketio.send("stop")
    
if __name__ == "__main__":
    socketio.run(app)
