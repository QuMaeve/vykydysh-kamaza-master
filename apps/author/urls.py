from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='author'),
    path('create', views.create, name='author-create'),
    # path('edit/<int:id>', views.edit, name='author-edit')
]
