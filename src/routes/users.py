from flask import Blueprint, request
from src.db import db
from src.models.user import User

users_api = Blueprint('users', __name__, url_prefix='/api/users')

@users_api.route('/', methods=['GET'])
def list_user():
    query = db.session.query(User)
    cnt = query.count()
    users = query.all()
    return "\n".join([user.__repr__() for user in users]+["total users: {}".format(cnt)])

@users_api.route('/create', methods=['POST'])
def create_user():
    args = request.args
    print(request.get_json())
    # nickname = args.get('nickname')
    # user = User(nickname=nickname, tag="123")
    # db.session.add(user)
    # db.session.commit()
    return ''
