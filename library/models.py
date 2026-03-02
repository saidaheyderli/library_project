from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 

class Book(models.Model):
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE,
        ) 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    

