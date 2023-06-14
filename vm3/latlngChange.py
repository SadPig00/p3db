from database import Database
from flask import Flask, render_template, request
import json
import requests
import pandas as pd
app=Flask(__name__)
db = Database()
@app.route('/makeDat')
def makeDat():
    csvfile = db.executeAll("select * from tiltdata")
    pd.DataFrame(csvfile).to_csv("C:\\Users\\b17\\Documents\\tiltData.dat")
    return '';

@app.route('/latlngChange',methods=['POST'])
def getLatLng():
    addr = request.form.get('addr')
    channel = request.form.get('channel')
    print(addr)
    print(channel)
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 073a393656181c6073880062d3507191"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']
    print(float(match_first['y']), float(match_first['x']))
    db.execute("update latlng set lat='"+str(match_first['y'])+"',lng='"+str(match_first['x'])+"' where tilt='"+str(channel)+"'")
    db.commit()
    return '';
if __name__=='__main__':
    app.run(host='localhost',port=5500)



    