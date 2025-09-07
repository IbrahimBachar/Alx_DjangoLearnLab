from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.bookView, name='book-list'),
    path('bookDetails/', views.BookDetailView.as_view(), name='book-detail'),
]