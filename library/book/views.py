from django.shortcuts import render
from .models import Book
from order.models import Order

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def books_filter(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(name__icontains=query)
    return render(request, 'books/books_filter.html', {'books': books, 'query': query})

def books_by_user(request, user_id):
    orders = Order.objects.filter(user_id=user_id).select_related('book')
    books = [order.book for order in orders]
    return render(request, 'books/books_by_user.html', {'books': books})