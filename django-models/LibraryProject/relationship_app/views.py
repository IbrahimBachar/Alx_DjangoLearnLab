from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def display_books(request):
#     return render(request, 'books.html')

def bookView(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'books/list_books.html', context)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'