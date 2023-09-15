from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Personne(models.Model):
    password = models.CharField(default="salll", max_length=50)
    username = models.CharField(default=" ", max_length=50)
    email = models.EmailField(max_length=100, null=True)
    first_name = models.CharField(default=" ", max_length=50)
    last_name = models.CharField(default=" ", max_length=50)

    def __str__(self):
        return self.username + str(self.id)

class Visit(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateField()