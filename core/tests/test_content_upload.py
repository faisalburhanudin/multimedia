from django.test import TestCase, Client

from core.models import User


class ContentUploadTestCase(TestCase):

    def test_get_upload_not_login(self):
        response = self.client.get("/uploads")
        self.assertEqual(response.status_code, 401)

    def test_get_upload_login(self):
        user = User()
        user.username = "faisal"
        user.set_password("burhanudin")
        user.save()

        client = Client()
        client.login(username="faisal", password="burhanudin")
        response = client.get("/uploads")
        self.assertEqual(response.status_code, 200)

    def test_post_upload_not_login(self):
        response = self.client.post("/uploads")
        self.assertEqual(response.status_code, 401)