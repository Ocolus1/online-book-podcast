from django.contrib import admin
from .models import BookChapter, Podcast, Book


admin.site.register(BookChapter)
admin.site.register(Podcast)
admin.site.register(Book)