
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from library import settings
from django.contrib.auth import views
from apps.book.views import document_view
from library.settings import BASE_DIR

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='pages/authentication/login.html', redirect_authenticated_user=True), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('author/',  include('apps.author.urls')),
    path('user/',  include('apps.user.urls')),
    path('book/', include('apps.book.urls')),
    path('documents/', include('apps.file.urls')),
    path('issue/', include('apps.issue.urls')),
    path(f'{BASE_DIR}/<str:path>', document_view, name='media'),
    path('', include('apps.main.urls')),
]
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
