from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest

from .forms import BookForm
from .models import Book


# Create your views here.

def homepage(request):
    return render(request, 'Books/home.html')

@login_required(login_url='/user/login/')
def bookspage(request : HttpRequest):
    user = request.user
    books = Book.objects.filter(user = user).order_by('-id')
    # print(books)

    context = {'books':books}
    return render(request, 'Books/books.html',context)

@login_required(login_url ='/user/login/')
def createbookspage(request : HttpRequest):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title =form.cleaned_data.get('title' ),
                author =form.cleaned_data.get('author'),
                genre =form.cleaned_data.get('genre'),
                user = request.user
                )
            return redirect('books')

    context = {'form': form}
    return render(request, 'Books/createbook.html',context)

@login_required(login_url ='/user/login/')
def deletebook(request, bookid):
    Book.objects.get(id= bookid).delete()
    return redirect('books')


@login_required(login_url ='/user/login/')
def editbook(request :HttpRequest , bookid):
    book = Book.objects.get(id= bookid)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.filter(id = bookid).update(
                title= form.cleaned_data.get('title'),
                author= form.cleaned_data.get('author'),
                genre= form.cleaned_data.get('genre')
            )
            return redirect('books')


    context = {'form':form}
    return render(request, 'Books/editbook.html',context)
