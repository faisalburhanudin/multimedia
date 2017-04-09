from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import User
from core.models import Content


def avatar_tag(obj):
    return mark_safe('<img src="%s" width="150" height="150" />' % obj.avatar_100x100.url)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', avatar_tag)


def content_img_tag(obj):
    return mark_safe('<img src="%s" width="150" height="150" />' % obj.image_50x50.url)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', content_img_tag)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Content, ContentAdmin)
