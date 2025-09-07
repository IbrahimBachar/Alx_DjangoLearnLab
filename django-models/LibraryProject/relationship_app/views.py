from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def display_books(request):
#     return render(request, 'books.html')

def bookView(request):
    relationship_app = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class BookDetailView(ViewDetail):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'book'