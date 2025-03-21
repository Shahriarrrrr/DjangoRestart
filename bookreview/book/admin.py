from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'genre',
                    'isbn', 
                    'publication_date', 
                    'average_rating', 
                    'created_at', 
                    'updated_at')
