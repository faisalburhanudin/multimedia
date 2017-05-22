from django.shortcuts import render
from django.contrib.auth.models import User

from core.models import Content


def profile_view(request):
    """Home profile user"""
    username = request.GET.get("username")
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    contents = Content.objects.filter(author=user).all()
    return render(request, "profile.html", {"user": user, "contents": contents})
