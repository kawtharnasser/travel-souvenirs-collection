from django.contrib import admin

from .models import Book, Purchase, Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(Purchase)
admin.site.register(Genre)
