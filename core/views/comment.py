from django.http import HttpResponse
from django.shortcuts import redirect

from core.models import UserComment, Content


def send(request):
    if not request.user.is_authenticated():
        return HttpResponse('Unauthorized', status=401)

    content_id = request.GET.get("content_id")
    text = request.POST.get("text")

    # get content object
    content = Content.objects.get(id=content_id)

    # save comment
    user_comment = UserComment()
    user_comment.text = text
    user_comment.author = request.user
    user_comment.content = content
    user_comment.save()

    return redirect(content)
