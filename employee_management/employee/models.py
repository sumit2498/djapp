from django.db import models

# Create your models here.


#Name Of The Table
class Employee(models.Model):
  
  # Columns of the table
  empid = models.AutoField(primary_key = True)  
  first_name = models.CharField(max_length = 100, blank = False)
  last_name = models.CharField(max_length = 100,blank = False)
  address = models.CharField(max_length = 100)
  dob = models.DateField()
  mobile = models.IntegerField(unique=True)
  city = models.CharField(max_length = 100)