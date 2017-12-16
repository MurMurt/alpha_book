from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='books_list'),
    url(r'^book/(?P<id>\d+)', views.BookPageView.as_view(), name='book'),
    url(r'^books/$', views.BookList.as_view()),
    url(r'login/$', views.login),
    url(r'sign_in/$', views.signUp),
    url(r'logout/$', views.logout)
]
