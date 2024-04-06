from django.urls import path
# Импортируем созданное нами представление
from .views import BulletinList


urlpatterns = [
    # В данном случае путь к постам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', BulletinList.as_view(), name='bulletin_list'),
]
