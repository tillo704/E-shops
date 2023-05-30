from django.db import models
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=160)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10000000, decimal_places=2)
    address = models.CharField(max_length=150)
    phone_number= PhoneNumberField(unique=True)
    tg_username = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self) :
        return str(self.title)
    
    class Meta:
        ordering = ('-id',)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "Comment of"+str(self.author.username)