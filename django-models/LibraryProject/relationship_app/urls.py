from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.bookView, name='book-list'),
    path('libraryDetails/', views.LibraryDetailView.as_view(), name='library-detail'),
]