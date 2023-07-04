from django.urls import path

from user.views import AuthorCreateView

urlpatterns = [
    path('create/', AuthorCreateView.as_view()),
]