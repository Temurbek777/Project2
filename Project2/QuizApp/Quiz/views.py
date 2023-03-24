from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def Func1(request):
    return render(request, 'index.html')


def PageNotFound(request, exception):
    return HttpResponseNotFound("<h6>Page Not Found</h6>")


def Login(request):
    return HttpResponse('Login')
