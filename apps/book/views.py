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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from apps.book.models import Book
from apps.book.forms import BookForm, FilterBookForm

from library.settings import BASE_DIR, MEDIA_URL

import uuid

@login_required(login_url='login')
@permission_required('book.view_book', raise_exception=True)
def book_index(request):
    form_search = FilterBookForm(request.POST or None)
    # data = Book.objects.all().order_by('id')
    if request.method == 'POST':
        sort_name = request.POST['sort_name']
        sort_by = request.POST['sort_by']
        data = Book.objects.filter(
            Q(name__icontains=sort_name) |Q( author_id__first_name__icontains=sort_name)).order_by(sort_by)
    else:
        data = Book.objects.all().order_by('-id')

    paginator = Paginator(data, 10)
    page = request.GET.get('page', 1)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(
        request, 
        'pages/book/index.html', 
        {'data': data,'form_search':form_search,})

@login_required(login_url='login')
@permission_required('book.view_book', raise_exception=True)
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
            
            book_create.doc_path = f"{MEDIA_URL}documents/{filename}"
            book_create.save()
            messages.success(request, 'Запись успешно создана')
            return redirect('book-create')
        else:
            messages.error(request, 'Введите корректные данные')
    return render(request, 'pages/book/create.html', {'form': form})

@login_required(login_url='login')
@permission_required('book.change_book', raise_exception=True)
def book_edit(request, id):
    data = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=data) 
    if request.method == 'POST':
        if form.is_valid():
            book_create = form.save()
            book_create.user_id = request.user
            book_create.save()
            if request.FILES:
                print(request.FILES)
                if 'doc_path' in request.FILES and 'cover_path'in request.FILES:
                    file = request.FILES['doc_path']
                    print(default_storage)
                    filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['doc_path']).split('.')[1].lower()}", ContentFile(file.read()))
                    print(filename)
                    book_create.doc_path = f"{filename}"
                    file = request.FILES['cover_path']
                    filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['cover_path']).split('.')[1].lower()}", ContentFile(file.read()))
                    print(filename)
                    book_create.cover_path = f"{filename}"
                    book_create.save()

                if 'doc_path' in request.FILES:
                    file = request.FILES['doc_path']
                    filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['doc_path']).split('.')[1].lower()}", ContentFile(file.read()))
                    print(filename)
                    book_create.doc_path = f"{filename}"
                    book_create.save()

                if 'cover_path' in request.FILES:
                    file = request.FILES['cover_path']
                    filename = default_storage.save(f"{str(uuid.uuid4())}.{str(request.FILES['cover_path']).split('.')[1].lower()}", ContentFile(file.read()))
                    print(filename)
                    book_create.cover_path = f"{filename}"
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
    