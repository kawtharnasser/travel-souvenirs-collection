from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Genre
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PurchaseForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title', 'author', 'publication', 'price', 'description', 'image']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['title', 'author', 'publication', 'price', 'description', 'image']

class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = '/books'


# Genre Classes
class GenreList(LoginRequiredMixin, ListView):
    model = Genre

class GenreDetail(LoginRequiredMixin,DetailView):
    model = Genre

class GenreCreate(LoginRequiredMixin,CreateView):
    model = Genre
    fields = '__all__'

class GenreUpdate(LoginRequiredMixin,UpdateView):
    model = Genre
    fields = ['name', 'color']

class GenreDelete(LoginRequiredMixin,DeleteView):
    model = Genre
    success_url = '/genres/'



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

@login_required
def books_index(request):
    # books = Book.objects.all()
    books = Book.objects.filter(user = request.user)
    return render(request, 'books/index.html', {'books': books})  

@login_required
def books_detail(request,book_id):
    book = Book.objects.get(id=book_id)

    purchase_form = PurchaseForm()

    genre_book_doent_have = Genre.objects.exclude(id__in = book.genres.all().values_list('id'))

    return render(request, 'books/detail.html', {
        'book':book,
        'purchase_form': purchase_form,
        'genres': genre_book_doent_have

    })

@login_required
def add_purchase(request, book_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.book_id = book_id
        new_purchase.save()
    return redirect('detail', book_id = book_id)


@login_required
def assoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.add(genre_id)
    return redirect('detail', book_id = book_id)

@login_required
def unassoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.remove(genre_id)
    return redirect('detail', book_id = book_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup- Please try again later'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html',context)