from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(upload_to='media/materials', default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Programme(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(upload_to='media/posts', default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

# Create your models here.
