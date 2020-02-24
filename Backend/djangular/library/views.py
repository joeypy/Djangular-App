from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
books = Book.objects.all()
output = ''
for book in books:
    output += f"We have { book.title } book in DB <br>"

class Books(View):
    def get(self, request):
        return HttpResponse(output)

def first(request):
        return render(request, template_name='library.html', context={'books': books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)