from django.db import models

# Create your models here.

class Message(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    color = models.CharField(max_length=255, default="red")

    def __str__(self):
        return self.message