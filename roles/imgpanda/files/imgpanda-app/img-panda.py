from flask import Flask, jsonify, send_file
import os
import random
from pymongo import MongoClient
import time

app = Flask(__name__)

pandaPics=os.listdir("resources/")

uri = 'mongodb://ori:daba@ds013405.mlab.com:13405/panda'
client = MongoClient(uri)
db = client.get_default_database()
gets = db['gets']

@app.route('/img-panda', methods=['GET'])
def imgPanda():
    pic = random.choice(pandaPics)
    now=time.strftime("%D %H:%M:%S")
    gets.insert({"tag" : "img-panda", "action" : "served a GET request", "time" : now})
    return send_file("resources/" + pic, mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
