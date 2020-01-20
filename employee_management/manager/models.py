from django.db import models

# Create your models here.

class Manager(models.Model):
  email = models.CharField(max_length=100,unique = True)
  first_name = models.CharField(max_length=100,blank=False)
  last_name = models.CharField(max_length=100,blank=False)
  password1 = models.CharField(max_length=50)
  password2 = models.CharField(max_length=50)
  address = models.CharField(max_length=100,blank=False)
  dob = models.DateField()
  company = models.CharField(max_length=100)
  