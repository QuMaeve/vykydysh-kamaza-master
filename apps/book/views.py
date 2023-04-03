from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import FileResponse
from django.http import HttpResponseForbidden

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from apps.book.models import Book
from apps.book.forms import BookForm

from library.settings import BASE_DIR, MEDIA_URL

import uuid

@login_required(login_url='login')
def book_view(request, id):
    data = Book.objects.get(id=id)
    return render(
        request, 
        'pages/book/view.html', 
        {'data': data,})

@login_required(login_url='login')
@permission_required('book.add_book', raise_exception=True)
def book_create(request):
    form = BookForm()
    if request.method == 'POST' and request.FILES:
        form = BookForm(request.POST)
        file1 = request.FILES['doc_path']
        print(file1)
        if form.is_valid():
            file = request.FILES['doc_path']
            filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['doc_path']).split('.')[1].lower()}", ContentFile(file.read()))
            print(filename)
            book_create = form.save()
            book_create.user_id = request.user
            book_create.deleted = 0
            book_create.doc_path = f"{MEDIA_URL}{filename}"
            book_create.save()
            messages.success(request, 'Запись успешно создана')
            return redirect('book-create')
        else:
            messages.error(request, 'Введите корректные данные')
    return render(request, 'pages/book/create.html', {'form': form})

@login_required(login_url='login')
@permission_required('book.add_book', raise_exception=True)
def book_edit(request, id):
    data = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=data) 
    # 
    if request.method == 'POST':
        #  and request.FILES
        # form = BookForm(request.POST or None, instance=data)
        # form = BookForm(request.POST)
        # file1 = request.FILES['doc_path']
        # print(file1)
        if form.is_valid():
            book_create = form.save()
            book_create.user_id = request.user
            book_create.deleted = 0
            book_create.save()
            if request.FILES:
                file = request.FILES['doc_path']
                filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['doc_path']).split('.')[1].lower()}", ContentFile(file.read()))
                print(filename)
                
                book_create.doc_path = f"{MEDIA_URL}{filename}"
                book_create.save()
            messages.success(request, 'Запись успешно сохранена')
            return redirect('book-edit',id)
        else:
            messages.error(request, 'Введите корректные данные')
    return render(request, 'pages/book/edit.html', {'form': form, 'data':data})

@login_required(login_url='login')
@permission_required('book.view_book', raise_exception=True)
def document_view(request,*args,**kwargs):
    if True:
        print(f"{BASE_DIR}{request.path}")
        return FileResponse(open(f"{BASE_DIR}{request.path}", 'rb'))
    else:
        return HttpResponseForbidden('Not authorized to access this media.')
    