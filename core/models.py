from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class UserInfo(models.Model):
    """User models detail"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='avatars')

    avatar_50x50 = ImageSpecField(source='avatar', processors=[ResizeToFill(50, 50)], format='JPEG',
                                  options={'quality': 60})

    avatar_100x100 = ImageSpecField(source='avatar', processors=[ResizeToFill(100, 100)], format='JPEG',
                                    options={'quality': 60})

    avatar_150x150 = ImageSpecField(source='avatar', processors=[ResizeToFill(150, 150)], format='JPEG',
                                    options={'quality': 60})


class Content(models.Model):
    title = models.CharField(max_length=80)

    description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='images')

    image_160x160 = ImageSpecField(source='image', processors=[ResizeToFill(160, 160)], format='JPEG',
                                   options={'quality': 80})

    image_320x220 = ImageSpecField(source='image', processors=[ResizeToFill(320, 220)], format='JPEG',
                                   options={'quality': 100})

    author = models.ForeignKey(User)

    @property
    def total_comment(self) -> int:
        """Get total comment in content"""
        return UserComment.objects.filter(content=self.id).count()

    @property
    def total_view(self) -> int:
        """Get total view in content"""
        return UserView.objects.filter(content=self.id).count()

    @property
    def total_like(self) -> int:
        """Get total like in content"""
        return UserLike.objects.filter(content=self.id).count()


class UserComment(models.Model):
    text = models.CharField(max_length=500)

    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)


class UserView(models.Model):
    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)


class UserLike(models.Model):
    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)
