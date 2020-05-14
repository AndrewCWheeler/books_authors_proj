from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.books),
    path('append_author', views.append_author),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors_detail/<int:author_id>', views.authors_detail),
    path('append_book', views.append_book),
    path('books', views.books_redirect),
]