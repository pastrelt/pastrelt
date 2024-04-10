Всем привет!

Название проекта - "Доска объявлений".
Проект разработан на основании задания:
Нам необходимо разработать интернет-ресурс для фанатского 
сервера одной известной MMORPG — что-то вроде доски объявлений. 
Пользователи нашего ресурса должны иметь возможность 
зарегистрироваться в нём по e-mail, получив письмо с кодом 
подтверждения регистрации. После регистрации им становится 
доступно создание и редактирование объявлений. Объявления 
состоят из заголовка и текста, внутри которого могут быть 
картинки, встроенные видео и другой контент. Пользователи 
могут отправлять отклики на объявления других пользователей, 
состоящие из простого текста. При отправке отклика пользователь 
должен получить e-mail с оповещением о нём. Также пользователю 
должна быть доступна приватная страница с откликами на его 
объявления, внутри которой он может фильтровать отклики по 
объявлениям, удалять их и принимать (при принятии отклика 
пользователю, оставившему отклик, также должно прийти уведомление).
Кроме того, пользователь обязательно должен определить объявление
в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, 
Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, 
Мастера заклинаний.
Также мы бы хотели иметь возможность отправлять пользователям 
новостные рассылки.


Работа проекта организована на основе cтека: Python, Django. 

Состоит проект Bulletin_board из папок (согласно принципов Django):
1. Bulletin_board - параметры системы,
2. bulletin - основное приложение,
3. protect - выход из проекта,
4. sign - аутентификация и регистрация,
5. static - шаблоны,
6. templates - представления,
7. db.sqlite3 - файл БД,
8. manage.py - файл запуска,
9. Project_diagram_Notice_board.drawio - файл схема строения таблиц,
10. README.md - описание проекта.

Запуск проекта:
1. установите приложения стека
2. перенесите проект
3. запустите виртульное окружение
4. перейдите в терминале в папку проекта
5. выполните команды:
pip install django-allauth
pip install django-ckeditor
6. выполните старт
python manage.py runserver  

Работа проекта:
После запуска Вы получите приглашение ввести свой почтовый адрес,
на него вы получите уникальный код регистрациию.
Вносите полученый код и наслаждайтесь общением с приложением.
Далее все как в задании.

Удачи.
