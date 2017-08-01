from django.shortcuts import redirect
from core.models import UserLike, Content


def send(request):
    content_id = request.GET.get("content_id")
    user = request.user

    # get content
    content = Content.objects.get(id=content_id)

    similar = UserLike.objects.filter(author=user, content=content)
    if not similar:
        user_like = UserLike()
        user_like.author = user
        user_like.content = content
        user_like.save()

    return redirect(content)


def unlike(request):
    content_id = request.GET.get("content_id")
    user = request.user

    # get content
    content = Content.objects.get(id=content_id)

    like = UserLike.objects.filter(author=user, content=content)
    like.delete()

    return redirect(content)
