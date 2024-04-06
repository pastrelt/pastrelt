from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Registration
import random
import string


# Функция генерации случайного кода регистрации.
def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Функция получения email пользователя и отпарвки ему случайного кода регистрации.
def register(request):
    if request.method == 'POST':
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
        # Не верно, надо послать на ппроверку кода
        return render(request, 'sign/confirm_registration.html', {'email': email})

    return render(request, 'sign/register.html')

# Проверка почты по едентификации кода подтверждения и обновление email пользователя в
# постоянную базу User. Очистка записи в таблице временного хранения данных.
def confirm_registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        confirmation_code = request.POST.get('confirmation_code')

        register_now = Registration.objects.filter(email=email,
                                                   confirmation_code=confirmation_code).first()

        if register_now:
            user = User.objects.create_user(username=email, email=email)
            register_now.delete()
            return render(request, 'bulletin/bulletin_choice.html')
        else:
            return render(request, 'sign/registration_failure.html')

    return redirect('register')


