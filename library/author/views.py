from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Author


def is_librarian(user):
    if user.is_authenticated:
        return user.role == 1
    return False

@user_passes_test(is_librarian)
def author_list(request):
    """
    Show information about all authors (librarian only).
    """
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


@user_passes_test(is_librarian)
def create_author(request):
    """
    Provide an opportunity to create a new author (librarian only).
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        if name and surname and patronymic:
            Author.objects.create(name=name, surname=surname, patronymic=patronymic)
            return redirect('author:author_list')

    return render(request, 'create_author.html')


@user_passes_test(is_librarian)
def delete_author(request, author_id):
    """
    Provide the ability to remove the author if they are not attached to any book (librarian only).
    """
    author = get_object_or_404(Author, id=author_id)
    if not author.books.exists():
        author.delete()
    return redirect('author:author_list')


