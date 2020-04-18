# -*- coding: utf-8 -*-
from src.db import db
from .base import Base

class Queue(Base):
    __tablename__ = 'queues'
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(150))
    remark = db.Column(db.String(150))
    close_time = db.Column(db.DateTime)
    quota = db.Column(db.Integer)
    rotate_mode = db.Column(db.Integer)
    interval = db.Column(db.Integer) # 轮换模式时的时间间隔
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # foreign key
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # relations
    comments = db.relationship('Comment', backref='queue', uselist=True, lazy=True) # one to many
    def __init__(self,owner_id, password,remark,close_time,quota,rotate_mode,interval=900):
        self.owner_id = owner_id
        self.password = password
        self.remark = remark
        self.close_time = close_time
        self.quota = quota
        self.rotate_mode = rotate_mode
        self.interval = interval
    def __repr__(self):
        return "Queue(id='%s'"%(self.id) +\
            "password='%s'"%(self.password) +\
            "remark='%s'"%(self.remark) +\
            "close_time='%s'"%(self.close_time) +\
            "quota='%s'"%(self.quota) +\
            "rotate_mode='%s'"%(self.rotate_mode) +\
            "interval='%s'"%(self.interval) +\
            "created_on='%s'"%(self.created_on) +\
            "updated_on='%s'"%(self.updated_on) +")"
