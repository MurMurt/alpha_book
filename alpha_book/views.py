from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from alpha_book.models import Book


def books_list(request):
    return render(request, 'alfabook/books_list.html', {})


class MainPageView(View):
    def get(self, request):
        data = {
            'top_books': [
                {'title': 'book #1', 'id': 1},
                {'title': 'book #2', 'id': 2},
                {'title': 'book #3', 'id': 3},
            ]
        }
        return render(request, 'alfabook/index.html', data)


class BookPageView(View):
    def get(self, request, id):
        data = {
            'book': {
                'id': id
            }
        }
        return render(request, 'alfabook/book.html', data)


class BookList(ListView):
    model = Book
    template_name = 'alfabook/books_list.html'
    context_object_name = 'books'