# -*- coding: utf-8 -*-
import os
import hashlib
import configparser
from flask import Flask, request
from .db import db
from datetime import datetime
import re
from .routes import users_api, wechat_api


app = Flask(__name__)

# `local`, `development`, `test`, `production`
env = os.environ.get('ENV', 'production')

# Read Configuration
app_config = configparser.ConfigParser()
app_config.read('config.ini')
app.config['SQLALCHEMY_DATABASE_URI'] = app_config['postgresql'][env]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialization
db.init_app(app)
app.register_blueprint(users_api)
app.register_blueprint(wechat_api)

@app.route("/hello/<name>")
def hello_there(name):

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name
    return content

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
