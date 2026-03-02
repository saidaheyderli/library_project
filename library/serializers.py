from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ["id",
            "first_name", 
            "last_name", 
            "birth_date", 
            "country", 
            "created_at"]
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "published_date",
            "price",
            "pages",
            "is_available",
            "author",
            "author_id",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        
        
        
        