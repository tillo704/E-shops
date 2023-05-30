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
        second_response = self.client.get("/users/profile/aadmin")
        self.assertEqual(second_response.status_code, 301)


        #login

        self.client.login(username= 'aadmin',password="tillo123")

        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username':'aadmin2',
                'first_name':'django2',
                'last_name':'django_p5',
                'email':'django@gmail.com',
                'phone_number':'+998748547964',
                'tg_username':'username',
                
            }
        )

