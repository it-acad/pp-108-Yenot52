from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import get_user_model

User = get_user_model()

# Handle post-registration actions (redirect, etc.)
# User Registration view
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role', '0')  # Default to '0' (ordinary user)

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken.')
            return redirect('authentication:register')

        # Create new user
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                        password=password)
        user.save()

        # Set the role, we will handle it later in your model's role management
        # Here we assume a custom `CustomUser` model with a role attribute (but Django defaults can work as well)

        # Redirect to login page after successful registration
        messages.success(request, 'User registered successfully.')
        return redirect('authentication:login')

    return render(request, 'authentication/register.html')


# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after login
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('authentication:login')

    return render(request, 'authentication/login.html')


# Logout view
def logout_view(request):
    logout(request)
    return redirect('authentication:login')  # Redirect to login page after logout

