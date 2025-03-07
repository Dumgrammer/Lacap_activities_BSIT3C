from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=60)
    middlename = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
