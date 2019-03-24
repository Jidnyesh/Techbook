from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True)
    likes = models.ManyToManyField(User,related_name="posts")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now = True , auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)

    def __str__(self):
        return self.title
