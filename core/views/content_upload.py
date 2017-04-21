from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ContentUploadView(View):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated():
            return HttpResponse('Unauthorized', status=401)

        return render(request, "upload.html")

    @staticmethod
    def post(request):
        if not request.user.is_authenticated():
            return HttpResponse('Unauthorized', status=401)

        return render(request, "upload_succes.html")
