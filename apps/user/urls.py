from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='user'),
    path('user_index', views.user_index, name='user_index'),
    path('teacher', views.index_teacher, name='teacher'),
    path('create', views.create, name='user-create'),
    # path('add/<int:id>', views.add_issue, name='add-issue'),
    path('import', views.import_user, name='import'),
    path('import_teacher', views.import_teacher, name='import_teacher'),
    
]