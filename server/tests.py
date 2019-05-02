import unittest
from server import app, connect_db
import json
import requests
from mock import patch, MagicMock

class FlaskTestCase(unittest.TestCase):
    def test_list(self):
        tester = app.test_client(self)
        response = tester.get('/list', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    @patch('requests.post')
    def test_add(self, mock_post):
        tester = app.test_client(self)
        info = {"task": "test task"}
        response = tester.post('/add', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/delete?id=3', content_type='application/json')
        self.assertEqual(response.status_code, 200)    

    def test_complete(self):
        tester = app.test_client(self)
        response = tester.put('/complete?id=3', content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_not_found(self):
        tester = app.test_client(self)
        response = tester.get('/test', content_type='application/json')
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()        