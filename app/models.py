from django.db import models

# Create your models here.
class PopularMenu(models.Model):
    image=models.ImageField(upload_to='image/menu/popular', help_text="image size 86 X 86")
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=10, help_text="end with .00")
    

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    number_of_persons = models.IntegerField()
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

class ProductCategory(models.Model):
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/menu/ProductCategory', help_text="image size 86 X 86", blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=10, help_text="end with .00")
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
