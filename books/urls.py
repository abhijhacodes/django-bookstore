from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books.all'),
    path('<int:pk>', views.BookDetailView.as_view(), name='books.one'),
    path('<int:id>/review', views.review, name='book.review'),
    path('<str:author>', views.author, name='author.books')
]
