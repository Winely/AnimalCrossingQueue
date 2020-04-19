# -*- coding: utf-8 -*-
from src import db
from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, func, DateTime, Text

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer,primary_key=True)
    content = Column(Text) # 评论内容
    visitor_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    queue_id = Column(Integer, ForeignKey('queues.id'), nullable=False)
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    def __init__(self,content, visitor_id, queue_id):
        self.content = content
        self.visitor_id = visitor_id
        self.queue_id = queue_id
    def __repr__(self):
        return "Comment(id='%s'"%(self.id) +\
            "content='%s'"%(self.content) +\
            "created_on='%s'"%(self.created_on) +\
            "updated_on='%s'"%(self.updated_on) +")"
