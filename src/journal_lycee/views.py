from django.http import HttpResponse


def index(request):
    return HttpResponse("lorem isszpfihdiuofvgqhgsrguijqdsrmiogk")

def mainmenu(request):
    return HttpResponse("<h1>test<h1>")

def mainmenu(request):
    return HttpResponse("<h1>grostest<h1>")