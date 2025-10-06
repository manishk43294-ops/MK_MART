from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("This is contact page of shop")

def tracker(request):
    return HttpResponse("This is tracker page of shop")

def search(request):
    return HttpResponse("This is search page of shop")

def productview(request):
    return HttpResponse("This is productview page of shop")

def checkout(request):
    return HttpResponse("This is checkout page of shop")


