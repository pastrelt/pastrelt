from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    # Маршрут для отправки кода регистрации на введенный адрес почты.
    path('register/', views.register, name='register'),

    # Вод и подтверждение кода регистрации. Регистрация.
    path('confirm_registration/', views.confirm_registration, name='confirm_registration'),
]
