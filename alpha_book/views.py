from django.shortcuts import render

def books_list(request):
    return render(request, 'alfabook/books_list.html', {})
