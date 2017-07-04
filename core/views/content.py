from django.shortcuts import render

from core.models import Content, UserComment, UserView


def content_view(request, content_id):
    content = Content.objects.get(id=content_id)
    comments = UserComment.objects.filter(content=content)

    if request.user.is_authenticated and not UserView.objects.filter(author=request.user):
        user_view = UserView()
        user_view.author = request.user
        user_view.content = content
        user_view.save()

    return render(request, "content.html", {
        "content": content,
        "comments": comments,
        "link_like": "/like?content_id=%s" % content_id if request.user.is_authenticated else ''
    })
