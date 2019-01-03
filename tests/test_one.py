import unittest
from flask import json
from api.views.view import app

class TestOne(unittest.TestCase):

    def test_silly(self):
        self.assertTrue(True)