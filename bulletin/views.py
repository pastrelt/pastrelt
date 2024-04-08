from django.views.generic import ListView, CreateView
from .models import Bulletin
from .forms import BulletinForm
from django.shortcuts import render, redirect, reverse


def create_bulletin(request):
    # Заполняем форму ввода объявлений, записываем и
    # переходим на общий список объявлений.
    if request.method == 'POST':
        form = BulletinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/bulletin/')  # Перенаправляем на список объявлений
    else:
        # Получаем значение email из параметров URL для
        # получения id пользователя из User.
        email = request.GET.get('email')
        form = BulletinForm(email=email)
    return render(request, 'bulletin/bulletin_edit.html', {'form': form})


class BulletinList(ListView):
    # Выводит список всех объявлений.
    # Указываем модель, объекты которой мы будем выводить
    model = Bulletin
    # Поле, которое будет использоваться для сортировки объектов
    # Новости выводиться в порядке от более свежей к самой старой.
    ordering = '-date_and_time_bulletin'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'bulletin/bulletin.html'
    # Это имя списка, в котором будут лежать все объектыбазы.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'list_bulletin'
    paginate_by = 10  # количество записей на странице
