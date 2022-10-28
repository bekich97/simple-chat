from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="_")
    color = models.CharField(max_length=255, default="red")

    def __str__(self):
        return self.content