from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.hashers import check_password

from captcha.models import CaptchaStore
from rest_framework.authtoken.models import Token

from apps.auth.models import User


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post__with_valid_data__creates_usable_user(self):
        self.client.get(reverse('captcha-refresh'))

        captcha = CaptchaStore.objects.last()

        self.assertEquals(1, CaptchaStore.objects.count())
        self.assertEquals(0, User.objects.count())

        self.client.post(reverse('auth:signup'), {
            'username': 'pepe',
            'email': 'pepe@gmail.com',
            'password': 'H83s6d-$',
            'password2': 'H83s6d-$',
            'captcha_key': captcha.hashkey,
            'captcha': captcha.response,
        })

        self.assertEquals(1, User.objects.count())
        self.assertEquals(0, Token.objects.count())

        res = self.client.post(reverse('auth:get-token'), {
            'username': 'pepe',
            'password': 'H83s6d-$',
        })

        new_user = User.objects.last()

        self.assertTrue(check_password('H83s6d-$', new_user.password))

        self.assertEquals(1, Token.objects.count())
