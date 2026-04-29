import unittest
import json
from src.main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
    
    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
