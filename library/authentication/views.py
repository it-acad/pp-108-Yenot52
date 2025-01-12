from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = int(request.POST['role'])

        if not email or not password:
            return render(request, 'authentication/register.html', {'error': 'Email and password are required!'})

        user = CustomUser.objects.create(
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            role=role,
            is_active=True
        )
        return redirect('login')

    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('books_list')
        return render(request, 'authentication/login.html', {'error': 'Invalid email or password!'})

    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def is_librarian(user):
    return user.role == 1  # Librarian role

@user_passes_test(is_librarian)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'authentication/user_list.html', {'users': users})

@user_passes_test(is_librarian)
def user_detail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'authentication/user_detail.html', {'user': user})
