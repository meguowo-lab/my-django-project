from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from . import models


class WebTest(TestCase):
    def test(self):
        res = self.client.post(
            reverse("comments_create", args=["1"]), {"body": "1234test"}
        )
        self.assertRedirects(res, reverse("login"), status_code=302)

        res = self.client.login(username="rit", password="12345")
        print(res)

    @classmethod
    def setUpTestData(cls):
        Site(domain="localhost:8765").save()

        user = User.objects.create_superuser("rit", "", "12345")
        models.NewsPost(author=user, title="1234test", body="1234test").save()
