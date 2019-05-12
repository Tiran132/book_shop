from django.contrib import admin
from django.urls import path, include
from new_django_project.views import show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('categories.urls')),
    path('', include('buyers.urls')),
    path('', show_main_page),
]
