from django.db import models
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CustomUser(User):
    pass


class Book(models.Model):
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    number_of_pages = models.IntegerField()
    year_of_release = models.DateField()

    class Meta:
        unique_together = ('title', 'author')


class Comment(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField(default=5,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(1)
                                 ])
    text = models.TextField()

    class Meta:
        unique_together = ('user', 'book')
