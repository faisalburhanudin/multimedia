from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import login
from django.shortcuts import render, redirect
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
            return redirect("/")
        else:
            return render(request, "login.html", {"login_invalid": True})


def logout_view(request):
    """Logout user
    
    Success logout and redirect to home
    """
    logout(request)
    return redirect("/")
