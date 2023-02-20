from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here


class User(AbstractUser):
    avatar = models.ImageField(upload_to='img_profiles/%y/%m', default='img_profiles/23/01/prolie_default.png')
    cover_pic = models.ImageField(upload_to='img_profiles/%y/%m',default=None, null=True, blank=True)


class Post(models.Model):
    class Meta:
        ordering = ['-id']

    post_content = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img_post/%y/%m', default=None, null=True, blank=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null= False, blank= False)


class PostUSer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
