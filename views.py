from django.shortcuts import render
from django.http import  HttpResponse

def about(request):
    # return HttpResponse('Hi , I am Mohammad Ghanbari and this is my site')
    return render(request,'about.html')

def home(request):
    # return HttpResponse('This is home')
    return render(request,'home.html')

def Call(request):
    return HttpResponse('HI , How can I help you?')
