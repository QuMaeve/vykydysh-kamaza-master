from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='user'),
    # path('create/<int:id>', views.create_issue, name='create-issue'),
    # path('add/<int:id>', views.add_issue, name='add-issue'),
    path('import', views.import_user, name='import'),
    
]