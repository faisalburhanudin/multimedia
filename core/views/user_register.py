from django.shortcuts import render
from django.views import View


class UserRegister(View):

    @staticmethod
    def get(request):
        return render(request, "register.html")
