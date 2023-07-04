from rest_framework.generics import CreateAPIView
from user.models import Author
from user.serializers import AuthorCreateSerializer


class AuthorCreateView(CreateAPIView):
    model = Author
    serializer_class = AuthorCreateSerializer
