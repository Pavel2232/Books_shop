from rest_framework import permissions
from books.models import Book


class BooksAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, book: Book):
        if request.method in permissions.SAFE_METHODS:
            return Book.objects.filter(
                archived=False).exists()
        return request.user in book.authors.all()
