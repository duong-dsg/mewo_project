from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
