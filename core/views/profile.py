from django.shortcuts import render


def profile_view(request):
    """Home profile user"""
    return render(request, "profile.html")
