from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres_detail', kwargs={'pk':self.id})


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    publication =  models.CharField(max_length=200)
    price =  models.CharField(max_length=200)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id':self.id})

    def __str__(self):
        return self.title


class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"Purchased {self.book.title} on {self.purchase_date}"
    
