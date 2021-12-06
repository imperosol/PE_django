from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/<path:next_page>', views.login, name='login'),
    path('make_login/<path:next_page>', views.make_login, name='make_login'),
    path('create_account', views.create_account, name='create_account'),
    path('create_account/<path:next_page>', views.create_account, name='create_account'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up/<path:next_page>', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
