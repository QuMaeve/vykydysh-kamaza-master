from django.urls import path, include
from . import views



urlpatterns = [
    path('<str:path>', views.file_view, name='file'),

]