#from django.contrib.auth.models import User
#from django.views.generic.edit import CreateView
#from .models import BaseRegisterForm

# class BaseRegisterView(CreateView):
#     model = User
#     form_class = BaseRegisterForm
#     success_url = '/'

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Registration
import random
import string


# Функция генерации случайного кода.
def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def confirm_registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        confirmation_code = request.POST.get('confirmation_code')

        try:
            registration = Registration.objects.get(email=email, confirmation_code=confirmation_code)
            user = User.objects.create_user(email=email)
            user.save()
            registration.delete()
            return render(request, 'registration_success.html')
        except Registration.DoesNotExist:
            return render(request, 'register.html')

#
def register(request):
    if request.method == 'POST':
        print(1)
        email = request.POST.get('email')
        confirmation_code = generate_confirmation_code()

        Registration.objects.create(email=email, confirmation_code=confirmation_code)

        send_mail(
            'Код подтверждения',
            f'Ваш код подтверждения: {confirmation_code}',
            'passtreltsov@yandex.ru',
            [email],
            fail_silently=False,
        )

        return render(request, 'registration_success.html')

    return render(request, 'register.html')

# def confirm_registration(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         confirmation_code = request.POST.get('confirmation_code')
#
#         try:
#             registration = Registration.objects.get(email=email, confirmation_code=confirmation_code)
#             user = User.objects.create_user(email=email)
#             user.save()
#             registration.delete()
#             return render(request, 'registration_success.html')
#         except Registration.DoesNotExist:
#             return render(request, 'register.html')
#
#     return redirect('register')


