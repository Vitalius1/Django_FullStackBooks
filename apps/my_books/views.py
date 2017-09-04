from django.shortcuts import render, redirect
from .models import Book

def index(request):
    book_list = Book.objects.show_book()
    context = {
        'books':book_list
    }
    return render(request, "my_books/index.html", context)

def addBook(request):
    Book.objects.make_book(request.POST['title'], request.POST['category'], request.POST['author'])
    return redirect('/')
# Create your views here.
