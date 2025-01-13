from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Genre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PurchaseForm

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'publication', 'price', 'description', 'image']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication', 'price', 'description', 'image']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'


# Genre Classes
class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'

class GenreUpdate(UpdateView):
    model = Genre
    fields = ['name', 'color']

class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres/'



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})  

def books_detail(request,book_id):
    book = Book.objects.get(id=book_id)

    purchase_form = PurchaseForm()

    return render(request, 'books/detail.html', {
        'book':book,
        'purchase_form': purchase_form,
    })

def add_purchase(request, book_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.book_id = book_id
        new_purchase.save()
    return redirect('detail', book_id = book_id)
