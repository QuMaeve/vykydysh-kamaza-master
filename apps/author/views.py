from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from apps.author.models import Author
from apps.author.forms import AuthorForm

# Create your views here.
@login_required(login_url='login')
def create(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author_create = form.save()
            author_create.user_id = request.user
            author_create.save()
            messages.success(request, 'Автор успешно добавлен')
        else:
            messages.error(request, 'Введите корректные данные')
    return  render(request, 'pages/author/create.html', {'form': form})