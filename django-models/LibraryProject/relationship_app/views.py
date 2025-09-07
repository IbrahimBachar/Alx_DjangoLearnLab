from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView
from .views import list_books

# Create your views here.
# def display_books(request):
#     return render(request, 'books.html')

def bookView(request):
    relationship_app = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(ViewDetail):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'book'