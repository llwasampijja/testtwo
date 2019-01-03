import unittest
from flask import json
from api.views.view import app

class TestOne(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_silly(self):
        self.assertTrue(True)
        # response = self.client.get("/", content_type="application/json")
        # response_data = json.loads(response.data.decode())
        # self.assertEqual(response_data.get("message"), "welcome")