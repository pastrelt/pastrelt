from django.views.generic import ListView, CreateView
from .models import Bulletin
from .forms import BulletinForm, CommentForm, NewsForm
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail


# Делаем рассылку.
# Рассылку может производить зарегистрированный пользователь со статусом - супервизор.
def newsletter(request):
    # Пишем отклики, записываем и переходим на общий список объявлений.
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news_instance = form.save()

            # Находим пользователей с объявлениями в заданной категории
            users_with_bulletins = User.objects.filter(bulletin__category_bulletin=news_instance.category_news)

            # Отправляем письмо каждому пользователю
            for user in users_with_bulletins:
                send_mail(
                    'Новости в категории {}'.format(news_instance.category_news),
                    news_instance.text_news,
                    'passtreltsov@yandex.ru',
                    [user.email],
                    fail_silently=False,
                )
            # Перенаправляем на список объявлений
            return redirect('http://127.0.0.1:8000/bulletin/')
    else:
        # Получаем значение email из параметров URL для
        # получения id пользователя из User.
        email = request.GET.get('email')
        form = NewsForm(email=email)
    # Перенаправляем на форму ввода сомментарий.
    return render(request, 'news/newsletter.html', {'form': form})


# Добавляем сомментарии с существующим объявлениям.
def create_comment(request):
    # Пишем отклики, записываем и переходим на общий список объявлений.
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправляем на список объявлений
            return redirect('http://127.0.0.1:8000/bulletin/')
    else:
        # Получаем значение email из параметров URL для
        # получения id пользователя из User.
        email = request.GET.get('email')
        form = CommentForm(email=email)
    # Перенаправляем на форму ввода сомментарий.
    return render(request, 'comment/create_comment.html', {'form': form})


# Добавляем объявления.
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

# Просмотр списка Объявлений
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
