from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'order': order})

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my_orders.html', {'orders': orders})

def create_order(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        Order.objects.create(user=request.user, book=book)
        return redirect('my_orders')
    return render(request, 'orders/create_order.html', {'book': book})

def close_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = 'closed'
        order.save()
        return redirect('orders_list')
    return render(request, 'orders/close_order.html', {'order': order})
