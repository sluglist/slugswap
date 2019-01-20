from django.shortcuts import render
from django.http import HttpResponse
from Main.models import Book
from django.contrib.auth import logout


def index(request):
    context = {
    }
    #if request.user.is_authenticated else []
    return render(request, 'hi.html', context)

def login(request):
    return HttpResponse('Login')
    
def logout(request):
    logout(request)
    return HttpResponse('TestingLogout')
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
	if request.method == "POST":
		pass
	elif request.method == "GET":
		context = {'direction' : direction}
		return render(request, 'AddItem.html', context)

def sold(request):
    return HttpResponse('sold')

def comment(request, direction):
    return HttpResponse('comment')
