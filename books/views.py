from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from books.models import Book, Comment
from books.permissions import BooksAuthorPermission
from books.serializers import BookSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class ListBookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    search_fields = ['=authors__first_name']

    def get_queryset(self):
        return Book.objects.filter(archived=False)


class DetailBookView(RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer
    permission_classes = [BooksAuthorPermission, ]
    queryset = Book.objects.get_queryset()


class CommentView(ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ListMeBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Book.objects.filter(archived=False, authors__books__authors=self.request.user)
