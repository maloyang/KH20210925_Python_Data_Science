# -*- coding: utf-8 -*-

from flask import Flask, request, abort, render_template, Response
from flask import json, jsonify, session, redirect, url_for
#from flask_cors import CORS, cross_origin # for cross domain problem
from flask import send_file

import requests
import csv
import folium
import geocoder

#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route("/", methods=['GET'])
def basic_url():
    return 'hello'

@app.route("/hello", methods=['GET'])
def hello():
    name = request.args.get('name')
    return 'hello ' + name

@app.route("/map/kh-parking", methods=['GET'])
def map_kh_parking():
    url = "https://data.kcg.gov.tw/dataset/449e45d9-dead-4873-95a9-cc34dabbb3af/resource/fe3f93da-9673-4f7b-859c-9017d793f798/download/108.6.21.csv"
    r = requests.get(url)
    print(r)
    decoded_content = r.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    data_list = list(cr)

    # 開始產生地圖
    location = geocoder.osm('高雄市').latlng
    m = folium.Map(location=location, zoom_start=14)
    for item in data_list[1:]:
        try:
            name = item[2]
            total = item[7]
            fee = item[10]
            lat = item[5]
            lng = item[4]
            info = '%s<br>%s<br>停車格數：%s' %(name, fee, total)
            
            folium.Marker([float(lat), float(lng)], tooltip=info,
                        icon=folium.Icon(color='green', prefix='fa', icon='fa-car')).add_to(m)
            
        except Exception as e:
            print(e.args)    
            
    m.save('./map_kh_parking.html')

    return send_file('./map_kh_parking.html')


@app.route("/map/w01-6", methods=['GET'])
def map_w01_6():
    return app.send_static_file('W01-6.html')


if __name__ == "__main__":
    app.run()
