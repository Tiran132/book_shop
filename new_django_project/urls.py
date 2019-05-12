from django.contrib import admin
from django.urls import path, include
from new_django_project.views import show_main_page, show_books, show_book_details, show_categories, show_category_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('categories.urls')),
    path('', include('buyers.urls')),
    path('', show_main_page),
    path('books/', show_books),
    path('books/<int:book_id>/', show_book_details),
    path('categories/', show_categories),
    path('categories/<int:category_id>/', show_category_one),
]
