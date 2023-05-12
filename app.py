from flask import Flask,  request
app = Flask(__name__)

myseed = 0
@app.route('/',methods = ['POST', 'GET'])
def seeds():
    global myseed
    if request.method == 'GET':
       return str(myseed)
    else:
      content = request.get_json(silent=True)
      myseed = content['num']
      return "success"

       
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)