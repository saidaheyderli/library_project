from django.urls import path
from .views import (
    AuthorListAPIView,
    AuthorDetailAPIView,
    BookListAPIView,
    BookDetailAPIView,
)

urlpatterns = [
    path(
        "authors/",
         AuthorListAPIView.as_view(), 
         name="author-list-create"
    ),
    path(
        "authors/<int:author_id>/", 
        AuthorDetailAPIView.as_view(), 
        name="author-detail"
    ),

    path(
        "books/", 
        BookListAPIView.as_view(),
        name="book-list-create"
    ),
    path(
        "books/<int:book_id>/",
        BookDetailAPIView.as_view(), 
        name="book-detail"
    ),
]
