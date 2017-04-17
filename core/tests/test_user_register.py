from django.test import TestCase, Client

from core.models import User


# Create your tests here.
class UserRegisterTestCase(TestCase):

    def setUp(self):
        self.request = Client()

    def test_register_get(self):
        response = self.request.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_register_post(self):
        response = self.request.post("/register", data={
            "name": "Muhamad Faisal Burhanudin",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 200)

        users = User.objects.all()
        self.assertEqual(len(users), 1)

        user = users[0]
        self.assertEqual(user.username, "Muhamad Faisal Burhanudin")
