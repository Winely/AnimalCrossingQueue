# -*- coding: utf-8 -*-
from src.db import db

class Base(db.Model):
    __abstract__ = True
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
