from django.urls import path
# Импортируем созданное нами представление
from .views import BulletinList, create_bulletin


urlpatterns = [
    # В данном случае путь к постам у нас останется пустым.
    path('', BulletinList.as_view(), name='bulletin_list'),

    path('create/', create_bulletin, name='bulletin_create'),

    #path('bulletin/', BulletinList.as_view(), name='bulletin_list'),
    #
    # path('create/', create_bulletin, name='bulletin_create'),

]
