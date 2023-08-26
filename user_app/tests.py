from django.urls import reverse # https://docs.djangoproject.com/en/4.2/ref/urlresolvers/
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
import json

# from django.test import TestCase

class RegisterTest(APITestCase):

    def test_register(self):
        fake = Faker(['id_ID'])

        name = fake.user_name()
        email = fake.email()
        passw = name

        data = {
            'username' : name,
            'email': email,
            'password': passw,
            'password2': passw,
        }

        response = self.client.post(reverse('user_app:register'), data)
        # print(data, response.data, response.status_code, response.json())
        self.assertEqual(response.json()['status'], 201)


class LoginLogoutTest(APITestCase):

    def setUp(self):
        super().setUp()

        self.name = Faker().user_name()
        data = {
            'username' : self.name,
            'password' : self.name
        }
        self.user = User.objects.create_user(**data)
        self.token = Token.objects.get(user=self.user)

    def test_login(self):
        data = {
            'username': self.user.username,
            'password': self.name
        }
        # print('test login',data)

        response = self.client.post(reverse('user_app:login'), data)
        # print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_login2(self):
        self.client.login(username=self.name, password=self.name)
        # self.client.force_authenticate(user=None) # to force user unauthenticated
        # print('req2',self.client.request)

        response = self.client.get(reverse('watchlist_app:review.standard-list'))
        self.assertEqual(response.json()['status'], 200)

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key, halo='halo')
        # print('test logout', self.token.key)

        response = self.client.get(reverse('user_app:logout'))
        # print(response.json())
        self.assertEqual(response.status_code, 200)

class ReviewTest(APITestCase):
    def setUp(self):
        super().setUp()

        self.name = Faker().user_name()
        data = {
            'username' : self.name,
            'password' : self.name
        }
        self.user = User.objects.create_user(**data)
        self.token = Token.objects.get(user=self.user)

    def test_review_list(self):
        # define header must prefixed by HTTP_ and every _ after prefix will be -
        header = {
            'HTTP_AUTHORIZATION': 'Token '+self.token.key,
            'HTTP_HALO': 'halo'
        }
        # self.client.credentials(**header)

        # response = self.client.get(reverse('watchlist_app:review.standard-list'))
        response = self.client.get(reverse('watchlist_app:review.standard-list'), None, **header) # other way to pass header data

        self.assertEqual(response.json()['status'], 200)
        self.assertEqual(json.loads(response.content), {'status': 200, 'data': []}) # i just know, complex object can be compare too(in every language maybe)
