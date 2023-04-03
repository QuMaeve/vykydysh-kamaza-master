from library.settings import BASE_DIR

from django.http import FileResponse
from django.http import HttpResponseForbidden

from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
# @permission_required('object.view_object', raise_exception=True)
def file_view(request,*args,**kwargs):
    if True:
        return FileResponse(open(f"{BASE_DIR}{request.path}", 'rb'))
    else:
        return HttpResponseForbidden('Not authorized to access this media.')
    

