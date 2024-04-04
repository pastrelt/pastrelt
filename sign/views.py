from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

import random
import string


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

# Функция генерации случайного кода.
def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


from django.core.mail import send_mail
from django.shortcuts import render
from .models import Registration
#from .utils import generate_confirmation_code


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        confirmation_code = generate_confirmation_code()

        Registration.objects.create(email=email, confirmation_code=confirmation_code)

        send_mail(
            'Confirmation Code',
            f'Your confirmation code is: {confirmation_code}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        return render(request, 'registration_success.html')

    return render(request, 'register.html')


