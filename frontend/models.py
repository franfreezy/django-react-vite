from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    #this is a table in the database
    class Meta:
        ordering=['-reg_date']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
