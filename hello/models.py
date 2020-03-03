from django.db import models


# Create your models here.

class Sender(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.CharField(max_length=200)
    recipient = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    visible = models.IntegerField(default=1)
    timestamp = models.DateTimeField('date created')

    def __str__(self):
        return self.message
