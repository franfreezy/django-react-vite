from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    #this is a table in the database
    def __str__(self):
        return f"{self.first_name} {self.first_name}"
        
class registered(models.Model):
