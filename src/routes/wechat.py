# -*- coding: utf-8 -*-
import hashlib
from datetime import datetime
from flask import Blueprint, request, Response
from src.db import db
from src.services.wechat import parse_message_body
from src.utils import response_xml

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
    message = parse_message_body(body)
    return Response(
        response_xml({
            'ToUserName': message.to_user_name,
            'FromUserName': message.from_user_name,
            'CreateTime': int(datetime.now().timestamp())
            'MsgType': 'text',
            'Content': "hello, world",
        }),
        mimetype='text/xml'
    )
