from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# 1. Модель Category
# Категории объявлений — темы, которые они отражают (спорт, политика, образование и т. д.).
# Имеет единственное поле: название категории. Поле должно быть уникальным
# (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name_of_category = models.CharField(max_length=100, unique=True)

    # Выводит значение username при вызове.
    def __str__(self):
        return (self.name_of_category)

# 2. Модель News
# Модель для хранения новостей модератора, которые рассылаются подписчикам.
class News(models.Model):
    category_news = models.ForeignKey('Category', on_delete = models.CASCADE)
    title_news =  models.CharField(max_length = 255)
    text_news = models.TextField()
    date_and_time_news = models.DateTimeField(auto_now_add = True)


# 3. Модель Bulletin(Post)
# Эта модель должна содержать объявления, которые создают пользователи.
# Соответственно, модель должна включать следующие поля:
# автоматически добавляемая дата и время создания;
# связь «один ко многим» с моделью Category;
# автор объявления связь «один ко многим» с моделью User;
# заголовок объявления;
# текст объявления.
class Bulletin(models.Model):
    author_bulletin = models.ForeignKey(User, on_delete = models.CASCADE)
    title_bulletin =  models.CharField(max_length = 255)
    content = RichTextField()  # Используем RichTextField из django-ckeditor
    date_and_time_bulletin = models.DateTimeField(auto_now_add = True)
    category_bulletin = models.ForeignKey('Category', on_delete = models.CASCADE)

    # Форматирование вывода данных для вывода на основную страницу.
    def __str__(self):
        return (f'{self.title_bulletin.title()}   '
                f'{self.date_and_time_bulletin.strftime('%d-%m-%Y %H:%M:%S')}   '
                f'{self.content[:20]}')

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])


# 3.1 Модель BulletinCategory
# Промежуточная модель для связи «многие ко многим»:
# связь «один ко многим» с моделью Bulletin;
# связь «один ко многим» с моделью Category.
# class BulletinCategory(models.Model):
#     bulletin = models.ForeignKey('Bulletin', on_delete = models.CASCADE)
#     category = models.ForeignKey('Category', on_delete = models.CASCADE)


# 4. Модель Comment
# Каждое объявление может получить отклик.
# Модель будет иметь следующие поля:
# связь с объявлением «один ко многим» с моделью Bulletin(Post);
# автор объявления - связь «один ко многим» со встроенной моделью User,
# комментарии может оставить любой пользователь;
# текст комментария;
# дата и время создания комментария;
# флаг принятия;
# автор коментария - связь «один ко многим» со встроенной моделью User,
class Comment(models.Model):
    bulletin_key = models.ForeignKey('Bulletin', on_delete = models.CASCADE)
    text_comment = models.TextField()
    date_and_time_сomment = models.DateTimeField(auto_now_add=True)
    acceptance_flag = models.BooleanField(default = False)
    author_comment = models.ForeignKey(User,
                                       related_name='bulletin_comments',
                                       on_delete=models.CASCADE)