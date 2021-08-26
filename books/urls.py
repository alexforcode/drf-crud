from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet


app_name = 'books'

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    *router.urls,
]
