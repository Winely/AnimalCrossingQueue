from datetime import datetime
import unittest

from src.models import User, Queue
from src.utils import RotateMode


class ModelTestCase(unittest.TestCase):
    def test_create_queue(self):
        queue = Queue(owner_id="id", password="password", remark="remark", close_time=datetime.now(), quota=3,
                      rotate_mode=RotateMode.HARD)
        self.assertIsNotNone(queue)

    def test_user(self):
        user = User(nickname="Alice", tag="tag")
        self.assertIsNotNone(user)
