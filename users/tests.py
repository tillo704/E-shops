from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
# Create your tests here.



class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'django',
                'username':'aadmin',
                'email':'django@gmail.com',
                'password1':'tillo123',
                'password2':'tillo123',
            }
        )

        user= CustomUser.objects.get(username="aadmin")
        self.assertEqual(user.first_name,'django')
        self.assertEqual(user.email,'django@gmail.com')
        self.assertTrue(user.check_password,'tillo123')