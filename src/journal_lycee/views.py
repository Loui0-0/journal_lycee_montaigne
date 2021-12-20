from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Test 123 123 - Alex")

def mainmenu(request):
    return HttpResponse("<h1>test<h1>")

def mainmenu(request):
    return HttpResponse("<h1>grostest<h1>")
