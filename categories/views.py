from categories.models import Category
from django.http import HttpResponse


def show_categories(request):
    categories = Category.objects.all()
    result = ''

    for category in categories:
        books = category.books.all()
        result += f'<h1><a href="{category.id}">{category.name}</a> - {books.count()}</h1><br>'

    result += "<style>body{padding: 10px; margin: 0; font-family: sans-serif; background-color: #262626;} a, h1{font-size: 5vh; color: #eee;}</style>"
    return HttpResponse(result)


def show_one_category(request, category_id):
    category = Category.objects.get(id=category_id)
    books = category.books.all()
    result = f'<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css">' \
             f'<h1 style="border-bottom: 0.1vh solid #eee;"><a><i class="fas fa-arrow-left"></i> {category.name}</h1>'
    for book in books:
        result += f'<h2 style="padding-left: 2vw;"><a style="color: #eee;" href="/books/{book.id}">{book.name}</a></h2>'
    result += "<style>body{padding: 10px; margin: 0; font-family: sans-serif; background-color: #262626; color: #eee;}</style>"
    return HttpResponse(result)
