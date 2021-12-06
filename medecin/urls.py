from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'medecin'
urlpatterns = [
    path('register/', views.ask_registering, name='ask_registering'),
    path('registered/', views.register_result, name='register_result'),
    path('show_registered/', views.show_register_result, name='show_registered'),
    path('check_requests/', views.check_requests, name='check_requests'),
    path('approve_requests/', views.approve_requests, name='approve_requests'),
    path('view_all/', views.view_all, name='view_all'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
