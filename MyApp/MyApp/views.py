# controller

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world!! I'm Learning Django")
    return render(request, 'website/index.html')
    
def about(request):
    #return HttpResponse("Hello, world!! This is my about page")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello there, this is contact page")
    return render(request, 'website/contact.html')
