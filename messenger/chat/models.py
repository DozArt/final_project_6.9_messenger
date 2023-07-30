from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nickname


class Chat(models.Model):
    title = models.CharField(max_length=255)
    founder = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='founder')  # основатель

    profiles = models.ManyToManyField(Profile, through='ChatUser')

    def __str__(self):
        return self.title


class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class ChatUser(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
