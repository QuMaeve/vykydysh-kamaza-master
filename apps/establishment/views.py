from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Establishment
from .forms import FilterEstablishmentForm, EstablishmentForm

from apps.user.models import CustomUser


@login_required(login_url='login')
@permission_required('establishment.view_establishment', raise_exception=True)
def index(request):
    form_search = FilterEstablishmentForm(request.POST or None)
    if request.method == 'POST':
        sort_name = request.POST['sort_name']
        sort_by = request.POST['sort_by']
        data = Establishment.objects.filter(
            name__icontains=sort_name).order_by(sort_by)
    else:
        data = Establishment.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'pages/establishment/index.html', 
                  {'data': data, 'form_search': form_search})


@login_required(login_url='login')
@permission_required('establishment.add_establishment', raise_exception=True)
def create(request):
    form = EstablishmentForm()
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно создана')
            return redirect('establishment')
        else:
            messages.error(request, 'Введите корректные данные')
    return render(request, 'pages/establishment/create.html', {'form': form})



@login_required(login_url='login')
@permission_required('establishment.view_establishment', raise_exception=True)
def view(request, id):
    data = get_object_or_404(Establishment, id=id)
    return render(request, 'pages/establishment/view.html', {'data': data})


@login_required(login_url='login')
@permission_required('establishment.change_establishment', raise_exception=True)
def edit(request, id):
    data = get_object_or_404(Establishment, id=id)
    form = EstablishmentForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные обновлены')
        else:
            messages.error(request, 'Введите корректные данные')
    return render(request, 'pages/establishment/edit.html', {'data': data,'form': form})


@login_required(login_url='login')
@permission_required('establishment.view_establishment', raise_exception=True)
def student(request, id):
    data = CustomUser.objects.filter(
        establishment_id=Establishment.objects.get(id=id), 
        groups__name__icontains='Ученики')
    return render(request, 'pages/establishment/student.html', {'data': data})


@login_required(login_url='login')
@permission_required('establishment.view_establishment', raise_exception=True)
def teacher(request, id):
    data = CustomUser.objects.filter(
        establishment_id=Establishment.objects.get(id=id), 
        groups__name__icontains='Преподаватель')
    return render(request, 'pages/establishment/teacher.html', {'data': data})
