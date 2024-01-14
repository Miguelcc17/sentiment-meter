from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  
    status = models.BooleanField(default=True) 

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    sentiment = models.CharField(max_length=255)
    emotion = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True) 