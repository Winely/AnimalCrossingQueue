# -*- coding: utf-8 -*-
from src.db import db
from .base import Base

class Comment(Base):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text) # 评论内容
    visitor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    queue_id = db.Column(db.Integer, db.ForeignKey('queues.id'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    def __init__(self,content, visitor_id, queue_id):
        self.content = content
        self.visitor_id = visitor_id
        self.queue_id = queue_id
    def __repr__(self):
        return "Comment(id='%s'"%(self.id) +\
            "content='%s'"%(self.content) +\
            "created_on='%s'"%(self.created_on) +\
            "updated_on='%s'"%(self.updated_on) +")"
