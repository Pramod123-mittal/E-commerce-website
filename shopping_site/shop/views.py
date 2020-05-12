from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'shop/index.html')
def about(request):
    #return render(request,'shop/index.html')
    return HttpResponse('we are at about views')
def contact(request):
    return HttpResponse('we are at contact page')
def tracker(request):
    return HttpResponse('we are at tracker page')
def search(request):
    return render(request,'shop/index.html')
def productView(request):
    return HttpResponse('we are at product view page')
def checkout(request):
    return HttpResponse('we are at checkout page')
