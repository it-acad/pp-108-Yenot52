from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from django.contrib.auth import get_user_model

def register(request):
    """
    Handles the registration of a new user. This allows users to register
    by providing their email, password, and other personal information.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = int(request.POST['role'])  # Assuming role is passed as an integer (0: visitor, 1: librarian)

        if not email or not password:
            return render(request, 'authentication/register.html', {'error': 'Email and password are required!'})

        user = CustomUser.objects.create(
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            role=role,
            is_active=True  # Automatically activate the user after registration
        )
        return redirect('login')  # Redirect to login page after registration

    return render(request, 'authentication/register.html')

def login_view(request):
    """
    Handles user login. Authenticates the user using email and password.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate using the email and password
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('books_list')  # Redirect to the books list or desired page
        return render(request, 'authentication/login.html', {'error': 'Invalid email or password!'})

    return render(request, 'authentication/login.html')

def logout_view(request):
    """
    Logs the user out and redirects to the login page.
    """
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def is_librarian(user):
    """
    Check if the user has the librarian role (role == 1).
    """
    return user.role == 1  # Assuming 1 represents the librarian role

@user_passes_test(is_librarian)
def user_list(request):
    """
    Displays a list of all users. Only accessible by users with librarian role.
    """
    users = CustomUser.objects.all()  # Get all users
    return render(request, 'authentication/user_list.html', {'users': users})

@user_passes_test(is_librarian)
def user_detail(request, user_id):
    """
    Displays the details of a single user. Only accessible by users with librarian role.
    """
    user = CustomUser.objects.get(id=user_id)  # Get the user by id
    return render(request, 'authentication/user_detail.html', {'user': user})

@login_required
@user_passes_test(is_librarian)
def user_detail_librarian(request, user_id):
    """
    Displays the details of a single user, only accessible by logged-in users with librarian role.
    """
    User = get_user_model()  # Dynamically gets the user model
    user = User.objects.get(id=user_id)  # Fetches the user
    return render(request, 'authentication/user_detail.html', {'user': user})
