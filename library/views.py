from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .paginations import StandardResultsPagination  


class AuthorListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()

        #filtering
        country = request.query_params.get("country")
        if country:
            authors = authors.filter(country=country)

        birth_year = request.query_params.get("birth_year")
        if birth_year:
            try:
                birth_year_int = int(birth_year)
                authors = authors.filter(birth_date__year=birth_year_int)
            except (ValueError, TypeError):
                pass

        #ordering (ignore invalid)
        ordering = request.query_params.get("ordering")
        allowed = ["last_name", "created_at", "birth_date"]
        if ordering:
            clean = ordering.lstrip("-")
            if clean in allowed:
                authors = authors.order_by(ordering)

        #pagination
        paginator = StandardResultsPagination()
        page = paginator.paginate_queryset(authors, request)
        serializer = AuthorSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):
    def get(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Author updated!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()

        author_id = request.query_params.get("author_id")
        is_available = request.query_params.get("is_available")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        year = request.query_params.get("year")
        search = request.query_params.get("search")
        ordering = request.query_params.get("ordering")
        
        if author_id:
            try:
                author_id_int = int(author_id)
                books = books.filter(author_id=author_id_int)
            except (ValueError, TypeError):
                pass

        if is_available:
            val = is_available.strip().lower()
            if val in ["true", "1", "yes"]:
                books = books.filter(is_available=True)
            elif val in ["false", "0", "no"]:
                books = books.filter(is_available=False)
            

        if min_price:
            try:
                books = books.filter(price__gte=min_price)
            except (ValueError, TypeError):
                pass

        if max_price:
            try:
                books = books.filter(price__lte=max_price)
            except (ValueError, TypeError):
                pass

        if year:
            try:
                year_int = int(year)
                books = books.filter(published_date__year=year_int)
            except (ValueError, TypeError):
                pass
            
        if search:
            books = books.filter(title__icontains=search)

        #ordering 
        allowed = ["price", "published_date", "created_at", "pages"]
        if ordering:
            clean = ordering.lstrip("-")
            if clean in allowed:
                books = books.order_by(ordering)

        #pagination
        paginator = StandardResultsPagination()
        page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book created successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book updated"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)