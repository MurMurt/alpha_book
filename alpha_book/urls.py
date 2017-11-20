from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='books_list'),
    url(r'^book/(?P<id>\d+)', views.BookPageView.as_view(), name='book')
]