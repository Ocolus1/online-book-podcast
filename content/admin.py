from django.contrib import admin
from .models import BookChapter, Book


admin.site.register(BookChapter)
admin.site.register(Book)