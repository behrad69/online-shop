from django.db import models
from django.contrib.auth.models import User
from commodity.models import product
# Create your models here.
class cart(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    color = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)