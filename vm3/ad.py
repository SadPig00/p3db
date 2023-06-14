import requests
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/sensor',methods=['POST'])
def getSensor():
    test = request.get_json()
    print(test, test['temp'], test['humi'])
    return ''
if __name__ =="__main__":
    app.run(port=5500,host='0.0.0.0')