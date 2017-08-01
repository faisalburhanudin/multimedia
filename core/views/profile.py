from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from core.models import Content, Profile


def profile_view(request):
    """Home profile user"""
    username = request.GET.get("username")
    if username:
        user = User.objects.get(username=username)
    elif request.user.is_anonymous() is False:
        user = request.user
    else:
        return HttpResponse("Not Found", status=404)

    contents = Content.objects.filter(author=user).all()
    return render(request, "profile.html", {"user": user, "contents": contents})


class RegisterUploadView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated():
            HttpResponse('Unauthorized', status=401)

        return render(request, "register.html")

    @staticmethod
    def post(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        avatar = request.FILES.get("avatar")

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()

        profile = Profile()
        profile.user = user
        profile.avatar = avatar
        profile.save()

        login(request, user)
        return redirect(profile)
