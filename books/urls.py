from django.urls import path
from rest_framework.routers import SimpleRouter

from books.views import ListBookView, DetailBookView, CommentView, ListMeBooksView
from rest_framework import routers

router: SimpleRouter = routers.SimpleRouter()
router.register(r'comment', CommentView)

urlpatterns = [
    path('', ListBookView.as_view()),
    path('<pk>', DetailBookView.as_view()),
    path('me/', ListMeBooksView.as_view()),
]
urlpatterns += router.urls
