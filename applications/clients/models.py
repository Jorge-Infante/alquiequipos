from django.db import models

# Create your models here.
class Client(models.Model):
    nit = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)