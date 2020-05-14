from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_books" : Book.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    title = request.POST["title"]
    desc = request.POST["desc"]
    Book.objects.create(
        title=title,
        desc=desc
    )
    return redirect('/')

def books(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        "title" : this_book.title,
        "desc" : this_book.desc,
        "id" : this_book.id,
        "authors" : this_book.authors.all(),
        "all_the_authors" : Author.objects.all(),
        "all_the_books" : Book.objects.all()
    }
    return render(request, 'books.html', context)

def append_author(request):
    author = request.POST["author_id"]
    book_id = request.POST["book_id"]
    this_book = Book.objects.get(id=book_id)
    additional_author = Author.objects.get(id=author)
    this_book.authors.add(additional_author)
    return redirect(f'/books/{book_id}')

def books_redirect(request):
    return redirect('/')

def authors(request):
    context = {
        "all_authors" : Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def add_author(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    notes = request.POST["notes"]
    Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        notes=notes
    )
    return redirect('/authors')

def authors_detail(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        "first_name" : this_author.first_name,
        "last_name" : this_author.last_name,
        "id" : this_author.id,
        "notes" : this_author.notes,
        "books" : this_author.books.all(),
        "all_the_books" : Book.objects.all(),
        "all_the_authors" : Author.objects.all()
    }
    return render(request, 'authors_detail.html', context)

def append_book(request):
    book = request.POST["book_id"]
    author_id = request.POST["author_id"]
    this_author = Author.objects.get(id=author_id)
    additional_book = Book.objects.get(id=book)
    this_author.books.add(additional_book)
    return redirect(f'/authors_detail/{author_id}')