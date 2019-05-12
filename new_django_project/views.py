from django.http import HttpResponse
from django.template.loader import render_to_string

from books.models import Book
from categories.models import Category


def show_main_page(request):
    categories = Category.objects.all()[:5]
    books = Book.objects.order_by('-id')[:10]

    result = render_to_string('index.html', {
        'title': 'TEST',
        'text': 'some text',
        'categories': categories,
        'books': books,
    })

    return HttpResponse(result)


def show_book_details(request, book_id):
    book = Book.objects.get(id=book_id)

    result = render_to_string('book.html', {
        'title': 'TEST',
        'text': 'some text',
        'book': book,
    })

    return HttpResponse(result)


def show_categories(request):
    categories = Category.objects.all()

    result = render_to_string('categories.html', {
        'title': 'TEST',
        'text': 'some text',
        'categories': categories,
    })

    return HttpResponse(result)


def show_books(request):
    books = Book.objects.all()

    result = render_to_string('books.html', {
        'title': 'TEST',
        'text': 'some text',
        'books': books,
    })

    return HttpResponse(result)


def show_category_one(request, category_id):
    category = Category.objects.get(id=category_id)
    books = category.books.all()

    result = render_to_string('category.html', {
        'title': 'TEST',
        'text': 'some text',
        'category': category,
        'books': books,
    })

    return HttpResponse(result)
