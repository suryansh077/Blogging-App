from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length=30)
    uemail = models.CharField(max_length=40)
    pwd = models.CharField(max_length=20)

    
    def __str__(self):
        return self.uname
    
class post(models.Model):
    name = models.CharField(max_length=30, default="")
    title = models.CharField(max_length=150)
    content = models.TextField()
    img = models.ImageField(default="")  


    def __str__(self):
        return self.title