from django.shortcuts import render,redirect
from book.forms import BookForm
from django.contrib import messages
from .models import Book

# Create your views here.

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Created Succesfully')
            return redirect('book-list')

    else:
        form =  BookForm()
    return render(request, 'book/book_form.html', {'form': form})    


def book_list(request):
    genre  = request.GET.get('genre')
    if genre:
        book = Book.objects.filter(genre = genre).order_by('-created_at')
    else:
        book = Book.objects.all().order_by('-created_at')
    return render(request, 'book/book_list.html',{"books" : book} )


def book_detail(request, pk):
    required_book = Book.objects.get(pk=pk)
    return render (request, 'book/book.html', {"book" : required_book})


def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Updated Succesfully')
            return redirect('book-update', pk=book.pk)
    else:
        form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {"form" : form})

def delete_book(request,pk):
    book = Book.objects.get(pk = pk)
    book.delete()
    return redirect('book-list')