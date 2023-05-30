from django.test import TestCase
from users.models import CustomUser
from .models import Category,Product

# Create your tests here.


class ProducttestCase(TestCase):
    def setUp(self):       
       user = CustomUser.objects.create(username='aadmin',email= 'django@gmail.com')
       user.set_password('my_pass')
       user.save()
       self.client.login(username='aadmin', password ='my_pass')

    
    def test_product_created(self):
        Category.objects.create(name='cat')
        response = self.client.post(
            '/products/new',
            data={
                'title':'my title',
                'price':123,
                'category':'1',
                'address':'pr address',
                'phone_number': '+998748547964',
                'tg_username': '@tillo704'
            }
        )
        product = Product.objects.get(id=1)
        self.assertEqual(product.title, 'my title')
        self.assertEqual(product.description, 'pr desc')
        self.assertEqual(product.price, 123)
        self.assertEqual(product.address, 'pr address')
        self.assertEqual(product.category.id, 1)


