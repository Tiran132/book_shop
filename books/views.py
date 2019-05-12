# from django.shortcuts import render
from books.models import Book
from django.http import HttpResponse

# Create your views here.


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'<a href="{book.id}/">{book.name}</a><br>'

    result += "<style>body{padding: 10px; margin: 0; font-family: sans-serif; background-color: #262626;} a{font-size: 5vh; color: #eee;}</style>"
    return HttpResponse(result)


def show_one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    result = f'<h1>{book.name}</h1><h3>price: {book.price}</3h><p>{book.description}</p>'
    result += "<style>body{padding: 10px; margin: 0; font-family: sans-serif; background-color: #262626; color: #eee;}</style>"
    return HttpResponse(result)
