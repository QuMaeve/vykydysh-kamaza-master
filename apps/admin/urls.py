from django.urls import path, include
from . import views



urlpatterns = [
    path('view/<int:id>', views.book_view, name='book-view'),
    # path('create/', views.document_create, name='document-create'),
    # path('edit/<int:id>', views.document_edit, name='document-edit'),
    # path('delete/<int:id>', views.document_delete, name='document-delete'),

    # path('api/', DocumentList.as_view(), name='api-document-gp'),
    # path(r'^upload/(?P<filename>[^/]+)$', DocumentList.as_view())

]