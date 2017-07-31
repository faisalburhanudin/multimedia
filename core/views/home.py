from django.core.paginator import Paginator
from django.shortcuts import render

from core.models import Content


# Create your views here.
def home(request):
    page = request.GET.get("page", 1)

    contents = Content.objects.order_by('-id')
    paginator = Paginator(contents, 21)

    return render(request, "home.html", {
        'contents': paginator.page(page),
        'pagination': 'pagination_home.html'
    })
