from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase


class UserLoginTestCase(TestCase):

    def test_login_get(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        user = User()
        user.username = "faisalburhanudin"
        user.set_password("123456")
        user.save()

        response = self.client.post("/login", data={
            "username": "faisalburhanudin",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)

        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated(), True)
