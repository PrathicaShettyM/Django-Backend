# import the django.http
from django.http import HttpResponse
from django.shortcuts import render


# simple methods for each route
def home(request):
    #return HttpResponse("Hello Django World!! This is my Home Page")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello Django World!! This is my About Page")

def contact(request):
    return HttpResponse("Hello Django World!! This is my Contact Page")
