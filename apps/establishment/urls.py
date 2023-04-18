from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='establishment'),
    path('create', views.create, name='establishment-create'),
    path('view/<int:id>', views.view, name='establishment-view'),
    path('edit/<int:id>', views.edit, name='establishment-edit'),
    path('student/<int:id>', views.student, name='establishment-student'),
    path('teacher/<int:id>', views.teacher, name='establishment-teacher'),
]