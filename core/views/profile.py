from django.shortcuts import render

from core.models import Content


def profile_view(request):
    """Home profile user"""
    user = request.user
    contents = Content.objects.filter(author=user).all()
    return render(request, "profile.html", {"user": user, "contents": contents})
