# -*- coding: utf-8 -*-
import os
import hashlib
from flask import Flask, request
from db import db
from models.user import User
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route('/', methods=['GET'])
def hello_world():
    args = request.args
    signature = args.get('signature')
    timestamp = args.get('timestamp')
    nonce = args.get('nonce')
    echostr = args.get('echostr')

    token = 'testToken'
    tmpstr = ''.join(sorted([token, timestamp, nonce])).encode('utf-8')
    hashcode = hashlib.sha1(tmpstr).hexdigest()
    if signature == hashcode:
        return echostr

@app.route('/api/users/create', methods=['GET'])
def create_user():
    args = request.args
    nickname = args.get('nickname')
    user = User(nickname=nickname, tag="123")
    db.session.add(user)
    db.session.commit()
    return nickname

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
