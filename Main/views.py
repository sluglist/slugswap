from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Home')

def login(request):
    return HttpResponse('Login')

def items(request, direction, catagory=None):
    return HttpResponse('Items')

def item(request, id):
    return HttpResponse('item')

def inbox(request):
    return HttpResponse('inbox')
