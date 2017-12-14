from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from alpha_book.forms import Login, RegisterForm, UserCreateForm, RegistrationForm
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

        return render(request, 'alfabook/book.html', {'username': auth.get_user(request).username,'book': data, 'comments': comments, 'rating': rating})


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
            return render(request, 'alfabook/login.html',args)
    else:
        return render(request, 'alfabook/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


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


class SignUp(FormView):
    template_name = 'alfabook/signin.html'
    form_class = UserCreateForm
    success_url = '/login/'


class Registration(FormView):
    template_name = 'alfabook/signin.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)
