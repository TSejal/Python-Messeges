from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 100)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
    
    def __str__(self):
        return self.first_name



class Message(models.Model):
    message_from = models.ForeignKey(User, related_name = "message_from")
    message_to = models.ForeignKey(User, related_name = "related_to")
    message = models.CharField(max_length = 140, null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"


    def __str__(self):
        return self.message