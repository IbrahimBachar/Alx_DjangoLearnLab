> > > from bookshelf.models import Book
> > > book = Book(title="1984", author="George Orwell", published_year=1949)
> > > book.save()
> > > Book.objects.all()
> > > <QuerySet [<Book: 1984>]>
> > > book = Book(title="Green City", author="Ibrahim Abdraman", published_year=2019)
> > > book.save()
> > > Book.objects.all()
> > > <QuerySet [<Book: 1984>, <Book: Green City>]>
> > > new_title = Book.objects.get(title="1984")
> > > new_title.update = "Nineteen Eighty-Four"
> > > Book.objects.all()
> > > <QuerySet [<Book: 1984>, <Book: Green City>]>

> > > new_title.title = "Nineteen Eighty-Four"
> > > new_title.save()  
> > > Book.objects.all()
> > > <QuerySet [<Book: Nineteen Eighty-Four>, <Book: Green City>]>
> > > delete = Book.objects.get(title="Green City")  
> > > delete.delete()
> > > (1, {'bookshelf.Book': 1})
> > > Book.objects.all()
> > > <QuerySet [<Book: Nineteen Eighty-Four>]>
