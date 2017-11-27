from django.contrib import admin

from .models import CustomUser, Book, Comment

admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(Comment)
