# -*- coding: utf-8 -*-
from .base import Base
from src.db import db
from src.utils import RotateMode
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

class Queue(Base):
    __tablename__ = 'queues'
    id = Column(Integer,primary_key=True)
    password = Column(String(150))
    remark = Column(String(150))
    close_time = Column(DateTime)
    quota = Column(Integer)
    rotate_mode = Column(Integer)
    interval = Column(Integer)  # 轮换模式时的时间间隔
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    # foreign key
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # relations
    comments = db.relationship('Comment', backref='queue', uselist=True, lazy=True) # one to many

    def __init__(self, owner_id, password, remark, close_time, quota, rotate_mode: RotateMode, interval=900):
        self.owner_id = owner_id
        self.password = password
        self.remark = remark
        self.close_time = close_time
        self.quota = quota
        self.rotate_mode = rotate_mode.value
        self.interval = interval

    def __repr__(self):
        return "Queue(id='{}'".format(self.id) +\
            "password='{}'".format(self.password) +\
            "remark='{}'".format(self.remark) +\
            "close_time='{}'".format(self.close_time) +\
            "quota='{}'".format(self.quota) +\
            "rotate_mode='{}'".format(self.rotate_mode) +\
            "interval='{}'".format(self.interval) +\
            "created_on='{}'".format(self.created_on) +\
            "updated_on='{}')".format(self.updated_on)
