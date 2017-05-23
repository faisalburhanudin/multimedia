from django.shortcuts import render

from core.models import Content


def content_view(request, content_id):
    content = Content.objects.get(id=content_id)
    return render(request, "content.html", {"content": content})
