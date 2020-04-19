# -*- coding: utf-8 -*-
from src.db import db
from src.utils import generate_random_str
from src.models import User


def create_user(nickname):
    tag = generate_random_str(6)
    try:
        user = User(nickname=nickname, tag=tag)
        db.session.add(user)
        db.session.commit()
    except Exception:
        return False
    return tag


def describe_user(tag):
    return User.query.filter_by(tag=tag).first()


def describe_user_by_id(id):
    return User.query.filter_by(id=id).first()


def describe_user_list(page_index, page_size):
    query = User.query.offset((page_index - 1) * page_size).limit(page_size)
    users = query.all()
    total = User.query.count()
    return users, total
