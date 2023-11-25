
import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Student(models.Model):
    
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user =models.OneToOneField("auth.User",on_delete=models.CASCADE)
   
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)


    def __str__(self):
        return self.full_name