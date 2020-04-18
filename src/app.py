# -*- coding: utf-8 -*-
import os
import hashlib
from flask import Flask, request
from .db import db
from datetime import datetime
import re
from .routes import users_api

app = Flask(__name__)
with open('postgresql.conf') as f:
    app.config['SQLALCHEMY_DATABASE_URI'] = f.read()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(users_api)


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
