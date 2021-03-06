from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import Content, Profile, UserComment


def avatar_tag(obj):
    return mark_safe('<img src="%s" width="150" height="150" />' % obj.avatar_100x100.url)


def content_img_tag(obj):
    return mark_safe('<img src="%s" width="150" height="150" />' % obj.image_160x160.url)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', content_img_tag, 'author')


class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'content')


admin.site.register(Content, ContentAdmin)
admin.site.register(Profile, )
admin.site.register(UserComment, UserCommentAdmin)
