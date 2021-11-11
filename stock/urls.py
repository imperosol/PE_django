from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'stock'
urlpatterns = [
    path('view_detail/', views.view_detail, name='view_detail'),
    path('view_global/', views.view_global, name='view_global'),
    path('add/', views.add, name='add'),
    path('added/', views.added, name='added'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
