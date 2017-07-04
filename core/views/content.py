from django.shortcuts import render

from core.models import Content, UserComment


def content_view(request, content_id):
    content = Content.objects.get(id=content_id)
    comments = UserComment.objects.filter(content=content)
    return render(request, "content.html", {
        "content": content,
        "comments": comments,
        "link_like": "/like?content_id=%s" % content_id if request.user.is_authenticated else ''
    })
