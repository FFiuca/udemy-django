from rest_framework.test import APITestCase

# you can create test file anywhere by extend APITestCase class
class CobaTest(APITestCase):

    def test_coba(self):

        self.assertEqual(200, 200)
