# -*- coding: utf-8 -*-
from flask import Blueprint, request
from src.utils import response_json
from src.db import db
from src.models.user import User
from src.services.user import create_user, describe_user_list

users_api = Blueprint('users', __name__, url_prefix='/api/users')

@users_api.route('/', methods=['GET'])
def list_user_api():
   args = request.args
   page_index = args.get('page_index')
   page_size = args.get('page_size')
   if page_index is None:
        page_index = 1
   if page_size is None:
        page_size = 10
   if page_size > 100:
        page_size = 100
 
   users, total = describe_user_list(page_index, page_size)
   users = [{
       'nickname': user.nickname,
       'tag': user.tag,
       'created_on': user.created_on
   } for user in users]
   return response_json(data={
        'list': users,
        'total': total,
   })

@users_api.route('/create', methods=['POST'])
def create_user_api():
    body = request.get_json()
    nickname = body['nickname']
    tag = create_user(nickname)
    if tag == False:
       return response_json(msg='Fail to create User', code=1)
    return response_json(data={'tag': tag})
