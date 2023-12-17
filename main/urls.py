from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListAPIView.as_view(), name="authors"),
    path('authors/<int:pk>/', views.AuthorRetrieveAPIView.as_view, name="author"),
    path('authors/create/', views.AuthorCreateAPIView.as_view(), name='author_create'),
    path('', views.BookListAPIView.as_view(), name="books"),
    path('books/<int:pk>/', views.BookRetrieveAPIView.as_view, name="book"),
    path('books/create/', views.BookCreateAPIView.as_view(), name='book_create')
]
