from rest_framework.viewsets import ModelViewSet

from .models import Author, Book
from .permissions import IsAdminUserOrReadOnly
from .serializers import AuthorSerializer, BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
