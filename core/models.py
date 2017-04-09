from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class User(models.Model):
    """User models detail"""
    name = models.CharField(max_length=100)

    avatar = models.ImageField(upload_to='avatars')

    avatar_50x50 = ImageSpecField(source='avatar', processors=[ResizeToFill(50, 50)], format='JPEG',
                                  options={'quality': 60})

    avatar_100x100 = ImageSpecField(source='avatar', processors=[ResizeToFill(100, 100)], format='JPEG',
                                    options={'quality': 60})


class Content(models.Model):
    title = models.CharField(max_length=80)

    description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='images')

    image_300x300 = ImageSpecField(source='image', processors=[ResizeToFill(300, 300)], format='JPEG',
                                   options={'quality': 80})

    author = models.ForeignKey(User)


class UserComment(models.Model):
    text = models.CharField(max_length=500)

    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)


class UserView(models.Model):
    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)
