from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    filter_backends = [filters.SearchFilter]
    search = search_fields = ['lastName', 'middle_name', 'dateOfBirth']
    serializer_class = AuthorSerializer


class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search = search_fields = ['title', 'author__name', 'genre']
    serializer_class = BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]