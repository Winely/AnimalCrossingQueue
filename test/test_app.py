import unittest
from src.app import home, hello_there


class AppTestCase(unittest.TestCase):
    def test_home(self):
        self.assertEqual(home(), "Hello, Flask!")