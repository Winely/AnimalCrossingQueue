# -*- coding: utf-8 -*-
from src.db import db
from .base import Base

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(150))
    tag = db.Column(db.String(150), unique=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # relations
    queue = db.relationship('Queue', backref='owner', uselist=False, lazy=True) # one to one
    comments = db.relationship('Comment', backref='visitor', uselist=True, lazy=True) # one to many
    def __init__(self,nickname,tag):
        self.nickname = nickname
        self.tag = tag
    def __repr__(self):
        return "User(id='%s'"%(self.id) +\
            "nickname='%s'"%(self.nickname) +\
            "tag='%s'"%(self.tag) +\
            "created_on='%s'"%(self.created_on) +\
            "updated_on='%s'"%(self.updated_on) +")"
