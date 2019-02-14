from django.http import HttpResponse


def index(request):
    return HttpResponse("Initial commit - samples app")
