from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.issue.models import Issue
from apps.issue.forms import IssueUserForm, IssueReportForm

from apps.book.models import Book
from apps.user.models import CustomUser
from apps.establishment.models import Establishment
from apps.locality.models import Locality
from django.db.models import Q
# from datetime import date
from dateutil.relativedelta import *
import datetime
from django.utils import timezone

from library.settings import BASE_DIR

from django.http import HttpResponse, JsonResponse
import xlwt



@login_required(login_url='login')
def index(request):
    data = Issue.objects.filter(
        user = CustomUser.objects.get(id=request.user.id), 
        end_time__gt = (datetime.date.today()).strftime("%Y-%m-%d")).order_by('id')
    print(data)
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(
        request, 
        'pages/bookshelf/index.html', 
        {'data':data,'base_dir':BASE_DIR})

@login_required(login_url='login')
def create_issue(request, id):
    if request.method == 'POST':
        if Issue.objects.filter(
            book = Book.objects.get(id=id),
            user = CustomUser.objects.get(id=request.user.id)).exists()==False:
            Issue.objects.create(
                book = Book.objects.get(id=id),
                user = CustomUser.objects.get(id=request.user.id),
                day_count = 14,
                end_time=(datetime.date.today()-relativedelta(day=+14)).strftime("%Y-%m-%d")
                )
            dc=Book.objects.get(id = id).count
            Book.objects.filter(id = id).update(
                count=dc-1
                )
            message = 'Книга добавлена на полку'
            print(message)
        else:
            message = 'Книга уже добавлена на полку'
            print(message)
        return redirect('main')
    
@login_required(login_url='login')
def add_issue(request, id):
    user = request.user
    form = IssueUserForm(user, request.POST or None)
    # form = IssueUserForm()
                        #  
                        #  initial={'student.queryset': CustomUser.objects.filter(
                        #                     deleted=False, 
                        #                     establishment = Establishment.objects.get(id=request.user.establishment.id),
                        #                     groups__name='Ученики')}
                                            
    users = CustomUser.objects.filter(deleted=False, groups__name='Ученики')
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            for student in form.cleaned_data.get("student"):
                if Issue.objects.filter(
                book = Book.objects.get(id=id),
                user = CustomUser.objects.get(id=student.id),
                deleted = False).exists()==False:
                    Issue.objects.create(
                        book = Book.objects.get(id=id),
                        user = CustomUser.objects.get(id=student.id),
                        day_count = 14,
                        end_time=(datetime.date.today()-relativedelta(day=+14)).strftime("%Y-%m-%d")
                        )
                    dc=Book.objects.get(id = id).count
                    Book.objects.filter(id = id).update(
                        count=dc-1
                        )
                    messages.success(request, 'Книга добавлена на полку '+ student.username)
                    print( 'Книга добавлена на полку '+ student.username)
                else:
                    messages.success(request, 'Книга уже была ранее добавлена на полку '+ student.username)
                    print( 'Книга уже была ранее добавлена на полку '+ student.username)
        else:
            messages.error(request, 'Книга не добавлена на полки ')
            print('Книга не добавлена на полки ')   

    return render(
        request, 
        'pages/bookshelf/add_issue.html', 
        {'data':users,'form':form,})

@login_required(login_url='login')
def report(request):
    current_tz = timezone.get_current_timezone()
    user = request.user
    initial_data = {
        'start_period' :(datetime.date.today()-relativedelta(months=+6)).strftime("%Y-%m-%d"), 
        'end_period' : datetime.date.today().strftime("%Y-%m-%d"),
    }
    print(initial_data)
    form = IssueReportForm(request.POST or None, initial = initial_data)
    users = CustomUser.objects.filter(deleted=False, groups__name='Ученики')
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():

            response = HttpResponse(content_type="application/ms-excel")
            response["Content-Disposition"] = f'attachment; filename="report_vydacha_{datetime.date.today().strftime("%Y-%m-%d")}.xls"'
            
            wb = xlwt.Workbook(encoding='cp-1251')

            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = [
                'Район',
                'Количество',
            ]
            ws = wb.add_sheet('Sheet1')
            row_num = 0
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
                
            ws.col(0).width = 256 * 36
            ws.col(1).width = 256 * 36
            font_style = xlwt.XFStyle()

            all_issue = Issue.objects.filter(
                start_time__range = [form.cleaned_data['start_period'],
                                     form.cleaned_data['end_period']])
            # print('all_issue:',all_issue.count())
            # for i in all_issue:
            #     print(i)
            locality = Locality.objects.all()
            for loc in locality:
                row_num += 1
                col_num = 0
                style = xlwt.easyxf(f'pattern: pattern solid, fore_colour white')

                # print('loc:',loc.name)
                issue = Issue.objects.filter(
                    start_time__range = [(form.cleaned_data['start_period']),form.cleaned_data['end_period']],
                    user_id__in = CustomUser.objects.filter(deleted=False, locality = loc))
                # print('loc:',issue.count())
                for value in {
                    "Район": loc.name,
                    "Количество": str(issue.count()),
                    }.values():
                        ws.write(row_num, col_num, value, style)
                        col_num += 1
            row_num += 1
            col_num = 0
            for value in {
                    "Район": "Без привязки к району",
                    "Количество": str(Issue.objects.filter(
                    start_time__range = [(form.cleaned_data['start_period']),form.cleaned_data['end_period']],
                    user_id__in = CustomUser.objects.filter(deleted=False, locality = None)).count()),
                }.values():
                    ws.write(row_num, col_num, value, style)
                    col_num += 1
                    
            row_num += 1
            col_num = 0
            for value in {
                    "Район": "Итого",
                    "Количество": str(all_issue.count()),
                }.values():
                    ws.write(row_num, col_num, value, style)
                    col_num += 1
                    
            messages.success(request, 'Отчёт сформирован')
            wb.save(response)
            return response

        else:
            messages.success(request, 'Введите корректные данные')
      

    return render(
        request, 
        'pages/admin/report.html', 
        {'data':users,'form':form,})