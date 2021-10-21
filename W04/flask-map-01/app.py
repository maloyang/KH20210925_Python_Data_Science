# -*- coding: utf-8 -*-

from flask import Flask, request, abort, render_template, Response
from flask import json, jsonify, session, redirect, url_for
#from flask_cors import CORS, cross_origin # for cross domain problem
from flask import send_file

import requests
import csv
import folium
import geocoder

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route("/", methods=['GET'])
def basic_url():
    return 'hello'


@app.route("/map/w01-6", methods=['GET'])
def map_w01_6():
    return app.send_static_file('W01-6.html')


if __name__ == "__main__":
    app.run()
