> > > from bookshelf.models import Book
> > > book = Book.objects.get(title="Green City")  
> > > book.delete()
> > > (1, {'bookshelf.Book': 1})