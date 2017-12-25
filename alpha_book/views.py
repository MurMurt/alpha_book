import base64
import json

import time
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from alpha_book.forms import Login, RegistrationForm, AddBookForm
from alpha_book.models import Book, Comment


def books_list(request):
    return render(request, 'alfabook/books_list.html', {})


class MainPageView(View):
    def get(self, request):
        data = Book.objects.filter(top=True)[:5]
        return render(request, 'alfabook/index.html', {'top_books': data, 'username': auth.get_user(request).username})


class BookPageView(View):
    def get(self, request, id):
        data = Book.objects.get(pk=id)
        comments = Comment.objects.filter(book=id)
        rating = sum(int(i.rating) for i in comments)
        if rating:
            rating /= len(comments)

        return render(request, 'alfabook/book.html',
                      {'username': auth.get_user(request).username, 'book': data, 'comments': comments,
                       'rating': rating})


class BookList(ListView):
    model = Book
    template_name = 'alfabook/books_list.html'
    context_object_name = 'books'


def BooksList(request):
    books = Book.objects.all()
    return render(request, "alfabook/books_list.html", {'books': books, 'username': auth.get_user(request).username})


def login(request):
    args = {}
    args['form'] = Login()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользовватель не найден'
            return render(request, 'alfabook/login.html', args)
    else:
        return render(request, 'alfabook/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


class UserCreateForm(object):
    pass


def signUp(request):
    # form = None;
    errors = []
    success = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']

            users = User.objects.all()
            usernames = []
            for x in users:
                usernames.append(x.username)

            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                errors.append('Пароли должны совпадать')
            elif usernames.count(username) != 0:
                errors.append('Такой логин уже занят')
            else:
                print("User")
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    # email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    # first_name=form.cleaned_data['first_name'],
                    # last_name=form.cleaned_data['last_name']
                )
                user.save()
                success += 'You was successfully registered.'
                return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()
    # form = RegistrationForm(request.POST)
    return render(request, 'alfabook/signin.html', {'form': form, 'errors': errors, 'success': success})


def create_res(msg, status):
    return HttpResponse(msg, content_type='application/json', status=status)


def add_comment(request):
    try:
        if request.method != 'POST':
            return create_res('Only POST', 400)
        print(request.body.decode('utf-8'))
        body = json.loads(request.body.decode('utf-8'))
        # body = json.loads('{"text":"asdf,mbadsf ,masdb fasjd","book":8}')
        print("LOLLO")
        if not auth.get_user(request).is_authenticated:
            print("PZDC")
            return create_res('', 400)

        # format, imgstr = body['img'].split(';base64,')
        # ext = format.split('/')[-1]
        # img = ContentFile(base64.b64decode(imgstr), name=str(round(time.time() * 1000)) + '.' + ext)
        # TODO
        comment = Comment.objects.create(user=auth.get_user(request).username, book=(body['book']),
                          rating=int(body['rating']), price=float(body['price']),
                          short_info=body['short_info'], image=0)
        comment.save()

        return create_res('{}', 200)
    except Exception as e:
        return create_res(e, 400)


def get_books(req):
    try:
        if req.method != 'GET':
            return create_res('Only Get', 400)

        limit = int(req.GET['limit'])
        offset = int(req.GET['offset'])

        if not limit and limit != 0 or not offset and offset != 0:
            return create_res('', 400)

        query_set = Book.objects.get_books(limit, offset)
        result = list()
        for book in query_set:
            p = {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                # 'company': book.company,
                # 'price': ','.join(str(book.price).split('.')),
                # 'short_info': book.short_info,
                # 'top': book.top,
                'img': book.image.url
            }
            result.append(p)
        return create_res(json.dumps(result), 200)
    except Exception as e:
        return create_res(e, 400)


def add_book(req):
    try:
        if req.method != 'POST':
            return create_res('Only POST', 400)

        body = json.loads(req.body.decode('utf-8'))

        if not auth.get_user(req).is_authenticated:
            return create_res('', 400)

        format, imgstr = body['img'].split(';base64,')
        ext = format.split('/')[-1]

        img = ContentFile(base64.b64decode(imgstr), name=str(round(time.time() * 1000)) + '.' + ext)
        try:
            book = Book.objects.create(title=body['title'], author=body['author'],
                                       year_of_release=int(body['year']), number_of_pages=int(body['pages']), image=img)
        except Exception as e:
            print(e)

        print("LOLOLOLO")
        book.save()

        return create_res('{}', 200)
    except Exception as e:
        return create_res(e, 400)
