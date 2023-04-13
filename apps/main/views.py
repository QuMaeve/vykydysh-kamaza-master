from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
# from .models import Locality
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.book.forms import BookForm, FilterBookForm
from apps.book.models import Book

# Create your views here.
@login_required(login_url='login')
def index(request):
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
 
    return render(request, 'pages/main/index.html', {'data':data, 'form_search':form_search,})