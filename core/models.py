from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    """User models detail"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='avatars')

    avatar_50x50 = ImageSpecField(source='avatar', processors=[ResizeToFill(50, 50)], format='JPEG',
                                  options={'quality': 60})

    avatar_100x100 = ImageSpecField(source='avatar', processors=[ResizeToFill(100, 100)], format='JPEG',
                                    options={'quality': 60})

    avatar_150x150 = ImageSpecField(source='avatar', processors=[ResizeToFill(150, 150)], format='JPEG',
                                    options={'quality': 60})

    def __str__(self):
        return self.user.username

    @staticmethod
    def get_absolute_url():
        return "/profile"


class Content(models.Model):
    title = models.CharField(max_length=80)

    description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='images')

    image_160x160 = ImageSpecField(source='image', processors=[ResizeToFill(160, 160)], format='JPEG',
                                   options={'quality': 80})

    image_320x220 = ImageSpecField(source='image', processors=[ResizeToFill(320, 220)], format='JPEG',
                                   options={'quality': 100})

    attachment = models.FileField(upload_to='attachments')

    content_type = models.CharField(max_length=10, default="")

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

    @property
    def attachment_ext(self):
        return self.attachment.file.name.split(".")[-1]

    def get_absolute_url(self):
        return "/content/%i" % self.id

    def __str__(self):
        return "%s" % self.title


class UserComment(models.Model):
    text = models.CharField(max_length=500)

    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)

    def __str__(self):
        return self.text


class UserView(models.Model):
    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)


class UserLike(models.Model):
    author = models.ForeignKey(User)

    content = models.ForeignKey(Content)
