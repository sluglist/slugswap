from django.shortcuts import render
from django.http import HttpResponse
from models import Book


def index(request):
    return HttpResponse('Home')

def login(request):
    return HttpResponse('Login')

def items(request, direction, catagory=None):
    return HttpResponse('Items')

def item(request, id):
	item = Book.objects.get(pk=id)[0]
    return HttpResponse(item)


def inbox(request):
    return HttpResponse('inbox')

def create(request, direction):
    return HttpResponse('create')

def sold(request):
    return HttpResponse('sold')

def comment(request, direction):
    return HttpResponse('comment')
