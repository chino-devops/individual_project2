from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.routes import costs
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestIndex(TestBase):

    def index(self):
        with requests_mock.mocker() as mocker:
            mocker.get('http://service_2:5000/get_brand', text="rolex")
            mocker.get('http://service_3:5000/get_material' ,text="platinum")
            mocker.post('http://service_4:5000/get_cost', text = '£45,000' )
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'a rolex made from platinum will cost £45,000', response.data)
            
            