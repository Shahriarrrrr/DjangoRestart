from django.urls import path
from book import views

urlpatterns = [
    path('book/new/',views.book_create, name= 'book-create'),
    path('book/list/',views.book_list, name= 'book-list'),
    path('book/<int:pk>/', views.book_detail, name= "book-detail"),
    path('book/<int:pk>/edit', views.book_update, name= "book-update"),
    path('book/<int:pk>/delete', views.delete_book, name= "book-delete"),
]
