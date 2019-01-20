from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Main.models import Book
import uuid

def index(request):
    user_wants = Book.objects.filter(want=True).all()
    user_has = Book.objects.filter(want=False).all()
    others_have = []
    others_want = []
    for w in user_wants:
        others_have += Book.objects.filter(name=w.name, want=False).all()
    for w in user_has:
        others_want += Book.objects.filter(name=w.name, want=True).all()
    context = {
        'user_wants': user_wants,
        'user_has': user_has,
        'others_want': others_want,
        'others_have': others_have,
    }
    return render(request, 'index.html', context)

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
        id=uuid.uuid4()
        listing = Book()
        listing.isbn = request.POST.get('bookISBN')
        listing.name = request.POST.get('bookName')
        listing.author = request.POST.get('bookAuthor')
        listing.course = request.POST.get('bookCourse')
        listing.publisher = request.POST.get('bookPublisher')
        if request.POST.get('bookCoverSoft') == True:
            if request.POST.get('bookCoverHard') == False:
                listing.hardcover = False
        elif request.POST.get('bookCoverHard') == True:
                listing.hardcover = True
        else:
            listing.hardcover = None
        listing.want = (request.POST.get('bookItemType') == 'want')
        listing.version = request.POST.get('bookVersion')
        listing.id = id
        listing.sold = False
        # listing.POSTer =  TODO NEED LOGIN
        print(listing.__dict__)
        listing.save()
        return redirect('/item/' + str(id))
    elif request.method == "GET":
        context = {'direction' : direction}
        return render(request, 'AddItem.html', context)

def sold(request):
    return HttpResponse('sold')

def comment(request, direction):
    return HttpResponse('comment')
