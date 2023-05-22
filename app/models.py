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
