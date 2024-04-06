from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
#from .views import BaseRegisterView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),

    #path('signup/', register, name='register'),
         # BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         # name='signup'),

    # Добавить новый маршрут для подтверждения регистрации и обработки кода подтверждения.
    path('register/', views.register, name='register'),
    path('confirm_registration/', views.confirm_registration, name='confirm_registration'),
]
