from django.db import models

# Create your models here.
class Pets(models.Model):
    name = models.CharField(max_length=250)
    breed = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    arrival_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images',null=True,blank=True)
    category = models.CharField(max_length=250)
    



