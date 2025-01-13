from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from book.models import Book  
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta


@login_required
def order_list(request):
    orders = Order.objects.all()  
    return render(request, 'order/order_list.html', {'orders': orders})


@login_required
def my_order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/my_order.html', {'orders': orders})


@login_required
def create_order(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user, 
            book=book, 
            plated_end_at=timezone.now() + timedelta(weeks=2)
        )  
        return redirect('order:my_order')  

    return render(request, 'order/create_order.html', {'book': book})


@login_required
def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        order.end_at = timezone.now()  
        order.save()
        return redirect('order:order_list') 

    return render(request, 'order/close_order.html', {'order': order})
