from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import render
from django.views import View


class UserLoginView(View):

    @staticmethod
    def get(request):
        return render(request, "login.html")

    @staticmethod
    def post(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

        return render(request, "login_success.html")
