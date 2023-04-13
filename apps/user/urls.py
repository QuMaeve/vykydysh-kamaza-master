from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='user'),
    path('teacher', views.index_teacher, name='teacher'),
    # path('create/<int:id>', views.create_issue, name='create-issue'),
    # path('add/<int:id>', views.add_issue, name='add-issue'),
    path('import', views.import_user, name='import'),
    path('import_teacher', views.import_teacher, name='import_teacher'),
    
]