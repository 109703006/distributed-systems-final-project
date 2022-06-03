from flask import Flask,request,redirect,url_for,render_template
from flask_socketio import SocketIO, emit
import configs

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
    print(place,time)
    return render_template("index.html", result="Result: ", score="?????????")
    
@app.route("/subscribe", methods=['POST'])
def subscribe():
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
