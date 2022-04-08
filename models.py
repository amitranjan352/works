
from django.db import models



class Snippet(models.Model):
    username=models.CharField(max_length=100)
    email  = models.EmailField(max_length=70,blank=True,unique=True)
    password =models.CharField(max_length=100)      

    


class Register(models.Model):
     
     
     username=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     password = models.CharField(max_length=100)

class Login(models.Model):
    username =models.CharField(max_length=100)
    password =models.CharField(max_length=100)





     




  