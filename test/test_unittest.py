import unittest
from src.app import home, hello_there

class Test_TestHome(unittest.TestCase):
    def test_home(self):
        self.assertEqual(home(), "Hello, Flask!")

    def test_hello_there(self):
        self.assertEqual(hello_there("Name"), "Hello there, Name")