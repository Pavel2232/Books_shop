from django.db import models
from user.models import Author


class Book(models.Model):
    authors = models.ManyToManyField(Author,related_name='books', verbose_name='Авторы')
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    archived = models.BooleanField(default=False, verbose_name='Архив')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    release = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор комментария')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name='Книга')
    text = models.TextField(verbose_name='Комментарий')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
