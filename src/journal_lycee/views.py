from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>tamere<h1>")

def mainmenu(request):
    return HttpResponse("<h1>test<h1>")