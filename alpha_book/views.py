from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from alpha_book.forms import Login, RegistrationForm
from alpha_book.models import Book, Comment


def books_list(request):
    return render(request, 'alfabook/books_list.html', {})


class MainPageView(View):
    def get(self, request):
        data = Book.objects.filter(top=True)[:4]
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


class SignUp(FormView):
    template_name = 'alfabook/signin.html'
    form_class = UserCreateForm
    success_url = '/'


def sign_in(request):
    args = {}
    # args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            return HttpResponseRedirect('/login/')
    else:
        args['form'] = UserCreationForm()
        return render(request, 'alfabook/signin.html', args)


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
