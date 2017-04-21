from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from core.forms.user_register import UserRegisterForm


class UserRegister(View):

    @staticmethod
    def get(request):
        return render(request, "register.html")

    @staticmethod
    def post(request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = request.POST["name"]
            user.set_password(request.POST["password"])
            user.save()

        return render(request, "register_success.html")
