from rest_framework import generics
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.utils import translation
from django.utils.translation import activate  # translation modulini import qilish


class BookPagination(PageNumberPagination):
    page_size = 2

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination


class BookListView(generics.ListAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


