from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, confirm_registration
#from .views import BaseRegisterView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/', register, name='register'),
         # BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         # name='signup'),
    path('confirm_registration/', confirm_registration, name='confirm_registration'),
]