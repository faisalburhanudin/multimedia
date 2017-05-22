from django.shortcuts import render


def content_view(request, content_id):
    return render(request, "content.html")
