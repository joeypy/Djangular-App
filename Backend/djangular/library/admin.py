from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['title', 'price', 'is_published']
    list_filter = ['published']
    search_fields = ['title', 'price']

    class Meta:
        model = Book
        fields = ['id', 'title',]

# admin.site.register(Book, BookAdmin)