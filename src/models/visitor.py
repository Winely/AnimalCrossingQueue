# -*- coding: utf-8 -*-
from src.db import db
from .base import Base

class Visitor(Base):
    __tablename__ = 'visitors'
    id = db.Column(db.Integer,primary_key=True)
    ordinal = db.Column(db.Integer) # 登记上岛的顺序
    land_status = db.Column(db.Boolean) # 登岛状态
    # foreign key
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    def __init__(self,ordinal,land_status=False):
        self.ordinal = ordinal
        self.land_status = land_status
    def __repr__(self):
        return "Visitor(id='%s'"%(self.id) +\
            "ordinal='%s'"%(self.ordinal) +\
            "land_status='%s'"%(self.land_status) +\
            "created_on='%s'"%(self.created_on) +\
            "updated_on='%s'"%(self.updated_on) +")"
