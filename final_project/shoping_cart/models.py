from django.db import models

# Create your models here.
class cart(models.Model):
    product_name = models.CharField(max_length=200, blank=False, null=False)
    quantity = models.IntegerField()
    