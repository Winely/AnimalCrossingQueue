# -*- coding: utf-8 -*-
import datetime
from src.db import db
from src.utils import generate_random_str, RotateMode
from src.models import Queue, User


def create_queue(**kwargs):
    if datetime.datetime.now().__gt__(kwargs.close_time):
        raise Exception('Closure Time must be greater than now')
    user = User.query.filter_by(tag=kwargs.owner_tag).first()
    if user is None:
        raise Exception('User not exist')
    try:
        queue = Queue(**kwargs)
        db.session.add(queue)
        db.session.commit()
    except Exception:
        return False
    return True
