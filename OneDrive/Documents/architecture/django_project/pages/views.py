from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Book
from .forms import BookForm
from .models import Book, Author
from accounts.views import admin_only
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
def homePageView(request):
    return HttpResponse ("Hello word")

def index(request):
    context={"message":"Hello from template"}
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))


@admin_only
def listBooks(request):
    context={"books":Book.objects.all().order_by("title")}
    return render(request,"listBooks.html",context)


def show (request,book_id):
    context={"book":get_object_or_404(Book,pk =book_id)}
    return render(request,"show.html",context)


def add (request):
    author=Author.objects.get(name="Victor Hugo")
    book=Book.objects.create(title="Dragon ball 3", quantity=12, author=author)
    return redirect("listBooks")

def edit (request):
    book = Book.objects.get(title ="Dragon ball 3")
    book.title="Dragon ball 6"
    book.save()
    return redirect("listBooks")


def remove (request):
    book = Book.objects.filter(title__startswith="Dragon")
    book.delete()
    return redirect("listBooks")


def add_with_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listBooks')
    else:
        form = BookForm() 

    return render(request, "book-form.html", {"form": form})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer