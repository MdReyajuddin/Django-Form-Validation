from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    active=models.BooleanField()
    created_on=models.DateTimeField()
    last_logged_in=models.DateTimeField()