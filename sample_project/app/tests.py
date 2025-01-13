from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_str(self):
        book = Book.objects.create(title="Django for Beginners", author="John Doe")
        self.assertEqual(str(book), "Django for Beginners")
