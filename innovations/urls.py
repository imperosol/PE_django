from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'stock'
urlpatterns = [
    path('innovation_1/', views.innovation_1, name='innovation_1'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
