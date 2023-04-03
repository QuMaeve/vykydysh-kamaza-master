from django.shortcuts import render, redirect

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from datetime import date
from dateutil.relativedelta import *

from apps.user.models import CustomUser
from apps.studentclass.models import Class
from apps.establishment.models import Establishment
from django.contrib.auth.models import Group
# from apps import class
# Import `xlrd`
# import xlrd
import re 
from openpyxl import load_workbook


# Create your views here.
@login_required(login_url='login')
def index(request):

    return render(
        request, 
        'pages/admin/import.html', 
        # {'data':users,'form':form,}
        )

@login_required(login_url='login')
def import_user(request):
    # Open a workbook 
    wb = load_workbook('documents/экспорт учащихся.xlsx')
    # workbook = xlrd.open_workbook('documents/экспорт учащихся.xlsx')
    sheet = wb.active
    # Retrieve cell value 
    sheet.cell(row=1, column=2).value
    school = Establishment.objects.filter(name=sheet.cell(row=1, column=1).value).first()
    # Print out values in column 2 
    for i in range(11, 25):
        print(i)
        if sheet.cell(row=i, column=1).value != None:
            classes = sheet.cell(row=i, column=1).value
            result = "".join(re.findall(r'\d+', classes))
            print(result)
            litera=""
            for d in classes:
                if d.isalpha():
                    litera = "".join(d)
            if litera !="":
                print(litera)
            if Class.objects.filter(number=int(result), 
                                    literature = litera,
                                    establishment = 
                                    Establishment.objects.filter(name=sheet.cell(row=1, column=1).value).first(),
                                    ).exists():
                a =Class.objects.filter(number=int(result), 
                                       literature = litera,
                                       establishment = 
                                        Establishment.objects.filter(name=sheet.cell(row=1, column=1).value).first(),
                                    ).first()
                print(a)
            else:
                a = Class.objects.create(number=int(result), 
                                     literature = litera,
                                     establishment = 
                                     Establishment.objects.filter(name=sheet.cell(row=1, column=1).value).first())
                print('Создан новый класс')
                print(Class.objects.get(id=a.id))
        first_name=''
        if sheet.cell(row=i, column=2).value != None:
            first_name = sheet.cell(row=i, column=2).value
            print(first_name)
        last_name=''
        if sheet.cell(row=i, column=3).value != None:
            last_name = sheet.cell(row=i, column=3).value
            print(last_name)
        patronymic=''   
        if sheet.cell(row=i, column=4).value != None:
            patronymic = sheet.cell(row=i, column=4).value
            print(patronymic) 
        login = first_name+'_'+last_name[0]+patronymic[0]
        print('login',login)
        date_joined = date.today().strftime("%Y-%m-%d")
        group = Group.objects.filter(name='Ученики').first()
        random_password = CustomUser.objects.make_random_password()

        u = CustomUser.objects.create(username = login, 
                                  password = random_password,
                                  is_superuser = False,
                                  date_joined = date_joined,
                                  is_active = True,
                                  is_staff = False,
                                  first_name=first_name,
                                  last_name=last_name,
                                  patronymic=patronymic, 
                                  classes=a, 
                                  establishment=school, )
        u.groups.add(group)
    return render(
        request, 
        'pages/admin/import.html', 
        # {'data':users,'form':form,}
        )