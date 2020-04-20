# -*- coding: utf-8 -*-
import hashlib
from flask import Blueprint, request
from src.db import db

wechat_api = Blueprint('wechat', __name__)

@wechat_api.route('/', methods=['GET'])
def wechat_validation():
    args = request.args
    signature = args.get('signature', '')
    timestamp = args.get('timestamp', '')
    nonce = args.get('nonce', '')
    echostr = args.get('echostr', '')

    token = 'testToken'
    tmpstr = ''.join(sorted([token, timestamp, nonce])).encode('utf-8')
    hashcode = hashlib.sha1(tmpstr).hexdigest()
    if signature == hashcode:
        return echostr
    return '4o4'

@wechat_api.route('/', methods=['POST'])
def wechat_message():
    body = request.get_data()
    print(body)
    return {}
