from flask import Flask,  request
from subprocess import Popen, PIPE
import socket
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def seeds():
# stress_cpu.py
    if request.method == 'GET':
       return str(socket.gethostname())
    else:
        subprocess.Popen(["python3", "stress_cpu.py"])



       
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)