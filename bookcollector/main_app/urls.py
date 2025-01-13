from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('books/<int:book_id>/add_purchase/', views.add_purchase, name='add_purchase'),

    #genre
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genres_update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genres_delete'),

    #Many to Many
    path('books/<int:book_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name ='assoc_genre'),
    path('books/<int:book_id>/unassoc_genre/<int:genre_id>/', views.unassoc_genre, name ='unassoc_genre'),    
    

]