from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    short = models.TextField(max_length=100, default=0)
    photo = models.ImageField(upload_to='media/materials', default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Programme(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    link = models.TextField(max_length=300, default=0)
    photo = models.ImageField(upload_to='media/posts', default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

# Create your models here.
