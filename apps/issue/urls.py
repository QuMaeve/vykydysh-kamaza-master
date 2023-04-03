from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='bookshelf'),
    path('create/<int:id>', views.create_issue, name='create-issue'),
    path('add/<int:id>', views.add_issue, name='add-issue'),
    path('report', views.report, name='report'),
    
]