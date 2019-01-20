from django.shortcuts import render
from django.http import HttpResponse
from Main.models import Book


def index(request):
    context = {
        'user_wants': [],
        'user_has': [],
        'others_want': [],
        'others_have': [],
    }
    return render(request, 'index.html', context)

def login(request):
    return HttpResponse('Login')

def items(request, direction, catagory=None):
    return HttpResponse('Items')

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
