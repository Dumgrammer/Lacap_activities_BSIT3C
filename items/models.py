from django.db import models

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=60)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)