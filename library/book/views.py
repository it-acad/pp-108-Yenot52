from django.shortcuts import render
from .models import Book
from order.models import Order

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'book': book})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def book_filter(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(name__icontains=query)
    return render(request, 'book/book_filter.html', {'book': book, 'query': query})

def book_by_user(request, user_id):
    orders = Order.objects.filter(user_id=user_id).select_related('book')
    books = [order.book for order in orders]
    return render(request, 'book/book_by_user.html', {'book': book})