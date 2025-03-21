from django.db import models

# Create your models here.

class Student(models.Model):
    stud_name = models.CharField(max_length=60)
    stud_email = models.CharField(max_length=200)
    stud_address = models.CharField(max_length=200, default="Address")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)