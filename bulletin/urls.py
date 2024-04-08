from django.urls import path
# Импортируем созданное нами представление
from .views import BulletinList, create_bulletin, create_comment


urlpatterns = [
    # В данном случае путь к постам у нас останется пустым.
    path('', BulletinList.as_view(), name='bulletin_list'),

    path('create/', create_bulletin, name='bulletin_create'),

    path('сomment/', create_comment, name='create_comment'),

    #path('bulletin/', create_comment, name='bulletin_choice'),
]
