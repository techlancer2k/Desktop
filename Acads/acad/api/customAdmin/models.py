from django.db import models

# Create your models here.

class CustomAdminData(models.Model):
    adminRollNo = models.IntegerField()
    adminPin = models.IntegerField(default=0)
    

def __str__(self):
    return self.adminRollNo

