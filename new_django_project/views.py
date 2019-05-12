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
