"""multimedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from core.views import home, user_login, content_upload, profile, content, comment, like
from multimedia import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.home, name="home"),
    url(r'^login', user_login.UserLoginView.as_view(), name='login'),
    url(r'^logout', user_login.logout_view, name='logout'),
    url(r'^uploads', content_upload.ContentUploadView.as_view(), name="upload"),
    url(r'^profile', profile.profile_view, name="profile"),
    url(r'^content/(?P<content_id>[0-9]{0,6})', content.content_view, name="content"),
    url(r'^comment$', comment.send),
    url(r'^like$', like.send),
    url(r'^search$', content.content_search),
    url(r'^register$', profile.RegisterUploadView.as_view(), name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
