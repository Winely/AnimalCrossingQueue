# -*- coding: utf-8 -*-
import datetime
from src.db import db
from src.utils import generate_random_str
from src.models import Queue, User

def create_queue(owner_tag, password, remark, close_time, quota=10, rotate_mode='timing', interval=900):
    if datetime.datetime.now().__gt__(close_time):
        raise Exception('Closure Time must be greater than now')
    user = User.query.filter_by(tag=owner_tag).first()
    if user is None:
        raise Exception('User not exist')
    try:
        queue = Queue(owner_id=user.id, password=password, remark=remark, close_time=close_time, quota=quota, rotate_mode=rotate_mode, interval=interval)
        db.session.add(queue)
        db.session.commit()
    except Exception:
        return False
    return True
