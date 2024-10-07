from django.db import models

# Create your models here.
class admindetails(models.Model):
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    