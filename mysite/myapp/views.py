from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse("Hello nerd")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    render(request, 'book_details.html', {'book': book})