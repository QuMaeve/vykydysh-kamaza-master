from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.book_index, name='book-index'),
    path('view/<int:id>', views.book_view, name='book-view'),
    path('create/', views.book_create, name='book-create'),
    path('edit/<int:id>', views.book_edit, name='book-edit'),
    # path('delete/<int:id>', views.document_delete, name='document-delete'),

    # path('api/', DocumentList.as_view(), name='api-document-gp'),
    # path(r'^upload/(?P<filename>[^/]+)$', DocumentList.as_view())

]