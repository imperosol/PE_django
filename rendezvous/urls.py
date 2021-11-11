from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'rendezvous'
urlpatterns = [
    path('select_patient/', views.select_patient, name='select_patient'),
    path('select_vaccin/', views.select_vaccin, name='select_vaccin'),
    path('vaccination_patient/', views.vaccination_patient, name='vaccination_patient'),
    path('insert/', views.insert, name='insert'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
