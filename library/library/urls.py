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
from django.urls import path
from . import views
from . import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('authors/', include('author.urls')),
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('filter/', views.book_filter, name='book_filter'),
    path('user/<int:user_id>/', views.book_by_user, name='book_by_user'),

    path('orders/', views.orders_list, name='orders_list'),
    path('orders/my/', views.my_orders, name='my_orders'),
    path('orders/create/<int:book_id>/', views.create_order, name='create_order'),
    path('orders/close/<int:order_id>/', views.close_order, name='close_order'),

    path('', views.orders_list, name='orders_list'),
    path('my/', views.my_orders, name='my_orders'),
    path('create/<int:book_id>/', views.create_order, name='create_order'),
    path('close/<int:order_id>/', views.close_order, name='close_order'),
    path('auth/', include('authentication.urls')),
    path('', include('book.urls')),
    path('books/', include('book.urls')),
    path('orders/', include('order.urls')),
]
