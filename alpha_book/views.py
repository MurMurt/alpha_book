from django.shortcuts import render
from django.views import View


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
