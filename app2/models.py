from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=(20))
    address = models.CharField(max_length=(100))
    salary= models.IntegerField()
    status = models.BooleanField()
