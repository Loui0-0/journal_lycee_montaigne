from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def mainmenu(request):
    return HttpResponse('<embed src="http://exo7.emath.fr/ficpdf/ficall.pdf" width="500" height="375">')
#http://exo7.emath.fr/ficpdf/ficall.pdf