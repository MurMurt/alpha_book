from django.contrib import admin

from .models import Book, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'number_of_pages', 'year_of_release', 'top')
    list_filter = ('author',)
    search_fields = ('author', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating')
    list_filter = ('user', 'book')
    search_fields = ('user', 'book')


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
