from django.shortcuts import render
from django.http import HttpResponse
from Main.models import Book


def index(request):
    return HttpResponse('Home')

def login(request):
    return HttpResponse('Login')

def items(request, direction, catagory=None):
    """Django reguest object"""
    if direction == 'want':
        checker = True
    else:
        checker = False
        
    testQuery = Book.objects.filter(want = checker).all()
    context = {'items' : testQuery}
    
    return render(request, 'ItemListings.html', context);

def item(request, id):
    id = str(id)
    item = Book.objects.get(pk=id)
    context = {'Book' : item}
    return render(request, 'Item.html', context)
    #return HttpResponse(item)


def inbox(request):
    return HttpResponse('inbox')

def create(request, direction):
    return HttpResponse('create')

def sold(request):
    return HttpResponse('sold')

def comment(request, direction):
    return HttpResponse('comment')
