from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView, name='book_list'),
]
