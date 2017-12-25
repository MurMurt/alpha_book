from django.db import models
from django import forms
from datetime import date, datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class BookManager(models.Manager):
    def get_books(self, limit, offset):
        return self.all()[offset:limit + offset]


class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    number_of_pages = models.IntegerField()
    year_of_release = models.IntegerField(default=datetime.now().year)
    top = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images', default='static/images/book.jpg')
    objects = BookManager()

    def __str__(self):
        return "{title}: {author}".format(title=self.title, author=self.author)

    class Meta:
        unique_together = ('title', 'author')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,  on_delete=models.CASCADE)
    rating = models.IntegerField(default=5,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(1)
                                 ])
    text = models.TextField()

    class Meta:
        unique_together = ('user', 'book')
