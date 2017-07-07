from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from core.models import Content
from core.tasks import resize


class ContentUploadView(View):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated():
            return HttpResponse('Unauthorized', status=401)

        return render(request, "upload.html")

    @staticmethod
    def post(request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        thumbnail = request.FILES.get("thumbnail")
        content_file = request.FILES.get("content")

        content = Content()
        content.title = title
        content.description = description
        content.image = thumbnail
        content.attachment = content_file
        content.author = request.user
        content.save()

        resize.delay(content.id, content.attachment.path)

        return redirect(content)
