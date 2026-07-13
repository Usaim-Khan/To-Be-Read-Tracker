from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('books/',views.bookspage, name='books'),
    path('create-book/',views.createbookspage, name= 'create-book'),
    path('delete-book/<int:bookid>', views.deletebook,name = 'delete-book'),
    path('edit-book/<int:bookid>', views.editbook,name = 'edit-book'),
]