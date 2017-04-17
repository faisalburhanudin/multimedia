from django.test import TestCase, Client


# Create your tests here.
class UserRegisterTestCase(TestCase):

    def setUp(self):
        self.request = Client()

    def test_register_get(self):
        response = self.request.get("/register")
        self.assertEqual(response.status_code, 200)
