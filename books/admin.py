from django.contrib import admin
from books.models import Author, Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author', 'get_number_of_comments')

    def get_author(self, book: Book):
        authors = [author.first_name for author in book.authors.only('first_name')]
        return authors

    def get_number_of_comments(self, book: Book):
        comment = len(book.comments.all())
        return comment

    get_author.short_description = 'Автор'
    get_number_of_comments.short_description = 'Кол-во комментариев'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_number_of_books', 'get_number_of_comments')

    def get_number_of_books(self, author: Author):
        books = len(author.books.all())
        return books

    def get_number_of_comments(self, author: Author):
        comments = len(author.comments.all())
        return comments

    get_number_of_comments.short_description = 'Кол-во комментариев'
    get_number_of_books.short_description = 'Кол-во книг'

