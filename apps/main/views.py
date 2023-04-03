from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from .models import Locality
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.book.forms import BookForm, FilterBookForm
from apps.book.models import Book

# Create your views here.
@login_required(login_url='login')
def index(request):
    # loc=Locality.objects.filter(
    #             id__in=UserLocality.objects.filter(
    #                 user_id=request.user.id).values_list('locality_id'))
    # family = loc
    # while loc:
    #     child = Locality.objects.filter(parent_id__in=loc)
    #     if not child :
    #         break
    #     else:
    #         family = family | child
    #         loc = child
    # if request.user.is_staff:
    #     data = Object.objects.filter(deleted=False).order_by('-id')
    # else:
    #     data = Object.objects.filter(
    #         deleted=False, lacality_id__in=family, 
    #         # organization_id__in=organization
    #         ).order_by('-id')
    data = Book.objects.filter(
        deleted=False, 
        # lacality_id__in=family, 
        # organization_id__in=organization
        ).order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'pages\main\index.html' , {'data':data,})