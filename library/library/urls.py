"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from book import views as book_views
from order import views as order_views
from authentication import views as auth_views
from author import views as author_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/', include('authentication.urls')),
    

    path('authors/', include('author.urls')),
    

    path('', book_views.book_list, name='book_list'),  
    path('<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('filter/', book_views.book_filter, name='book_filter'),
    path('user/<int:user_id>/', book_views.book_by_user, name='book_by_user'),

    path('orders/', order_views.order_list, name='order_list'),
    path('orders/my/', order_views.my_order, name='my_order'),
    path('orders/create/<int:book_id>/', order_views.create_order, name='create_order'),
    path('orders/close/<int:order_id>/', order_views.close_order, name='close_order'),

   
    path('books/', include('book.urls')),  
    path('orders/', include('order.urls')), 
]
