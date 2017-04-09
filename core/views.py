from django.shortcuts import render
from core.models import Content


# Create your views here.
def home(request):
    contents = Content.objects.all()
    return render(request, "home.html", {'contents': contents})
