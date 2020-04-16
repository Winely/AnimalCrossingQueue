# -*- coding: utf-8 -*-
from db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(150))
    tag = db.Column(db.String(150))
    def __init__(self,nickname,tag):
        self.nickname = nickname
        self.tag = tag
    def __repr__(self):
        return "User(id='%s'"%(self.id) +\
            "nickname='%s'"%(self.nickname) +\
            "tag='%s'"%(self.tag) +")"
