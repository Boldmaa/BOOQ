from django.contrib import admin

# Register your models here.

from .models import Tag, Book, Library

admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Library)