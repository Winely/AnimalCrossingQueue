import unittest
import os
from datetime import datetime

from src import app
from src.models.queue import Queue
from src.utils import RotateMode

TEST_DB_URI = "test.db"


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()
        self.assertFalse(app.debug)

    def test_list_user(self):
        pass

    def test_hello_world(self):
        response = self.app.get('/hello/Donggu')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello there, Donggu")

        response = self.app.get('/hello/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello there, Friend")

    def test_main_entry(self):
        param = {
            'signature': '6bcc1b0cd627090d0f0c294d8901a78253cf4d81',
            'echostr': '1560446583804254639',
            'timestamp': '1587269891',
            'nonce': '1633115511'
        }
        resp = self.app.get('/', query_string=param)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.decode('utf-8'), param['echostr'])
