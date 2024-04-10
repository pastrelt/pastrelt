from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from .models import Bulletin, Comment
from .forms import BulletinForm, CommentForm, NewsForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail


# Приватная страница комментарий, фильтрация, удаление,
# принятие, рассылка авторам  комментарий.
def private_page(request):
    email = request.GET.get('email', None)
    user = User.objects.get(email=email)
    user_id = user.id

    # Получаем все объявления автора и добавляем возможность сортировки по названию объявления
    bulletins_set = Bulletin.objects.filter(author_bulletin=user_id).order_by('title_bulletin')

    # Создаем список имен объявлений
    #bulletins = ', '.join(list(bulletins_set.values_list('title_bulletin', flat=True)))

    # Получаем все комментарии, относящиеся к объявлениям автора
    comments = Comment.objects.filter(bulletin_key__in=bulletins_set)

    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        action = request.POST.get('action')

        if action == 'accept':
            comment = get_object_or_404(Comment, id=comment_id)
            comment.acceptance_flag = True
            comment.save()

            # Отправляем уведомление автору комментария.
            author_comment = comment.author_comment
            bulletin_title = comment.bulletin_key.title_bulletin
            message = f'Добрый день! Ваш комментарий по объявлению - {bulletin_title}, принят'
            send_mail(
                'Принятие комментария',
                message,
                'passtreltsov@yandex.ru',
                [author_comment.email],
                fail_silently=False,
            )

        elif action == 'delete':
            comment = get_object_or_404(Comment, id=comment_id)
            comment.delete()

        else:
            bulletins_filter = request.POST.get('bulletins_filter')
            comments = comments.filter(bulletin_key__in=bulletins_set,
                                       bulletin_key__title_bulletin__icontains=bulletins_filter)

    context = {
        'user': user_id,
        'comments': comments,
        'bulletins': bulletins_set,
    }

    return render(request, 'page/private_page.html', context)


# Делаем рассылку новостей.
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
        form = NewsForm()
    # Перенаправляем на форму ввода сомментарий.
    return render(request, 'news/newsletter.html', {'form': form})


# Добавляем сомментарии к существующим объявлениям.
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
