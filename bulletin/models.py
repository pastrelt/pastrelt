from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 1. Модель Category
# Категории объявлений — темы, которые они отражают (спорт, политика, образование и т. д.).
# Имеет единственное поле: название категории. Поле должно быть уникальным
# (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name_of_category = models.CharField(max_length=100, unique=True)
    # Добавьте пользователю возможность подписываться на рассылку новостей в какой-либо категории.
    # Для этого добавьте поле subscribers (соотношение manytomany), в которое будут записываться пользователи,
    # подписанные на обновления в данной категории.
    subscribers = models.ManyToManyField(User, through = 'Categories_subscribers')

    # Выводит значение username при вызове.
    def __str__(self):
        return (self.name_of_category)

# 1.2 Модель Categories_subscribers
# Добавил вспомоательную модель при связи многие ко многим.
class Categories_subscribers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)


# # 2. Модель News
# # Модель для хранения новостей модератора, которые рассылаются подписчикам.
# class News(models.Model):
#     category_news = models.ManyToManyField('Category', through = 'PostCategory')
#     title_news =  models.CharField(max_length = 255)
#     text_news = models.TextField()
#     date_and_time_news = models.DateTimeField(auto_now_add = True)


# 3. Модель Bulletin(Post)
# Эта модель должна содержать объявления, которые создают пользователи.
# Каждое объявление имеет одну категорию.
# Соответственно, модель должна включать следующие поля:
# связь «один ко многим» с моделью Author;
# поле с выбором — «статья» или «новость»;
# автоматически добавляемая дата и время создания;
# связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# заголовок статьи/новости;
# текст статьи/новости;
# рейтинг статьи/новости.
# class Post(models.Model):
#     author = models.ForeignKey('Author', on_delete = models.CASCADE)
#     article_or_news = models.CharField(max_length=7, choices=[('статья', 'статья'), ('новость', 'новость')])
#     date_and_time = models.DateTimeField(auto_now_add = True)
#     category = models.ManyToManyField('Category', through = 'PostCategory')
#     title =  models.CharField(max_length = 255)
#     text_article_or_news = models.TextField()
#     rating = models.IntegerField(default = 0)
#
#     #  Превью статьи. Возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
#     def preview(self):
#         preview = self.text_article_or_news[:124] + '...'
#         return preview
#
#     # Форматирование вывода данных для вывода на основную страницу.
#     def __str__(self):
#         return (f'{self.title.title()}   '
#                 f'{self.date_and_time.strftime('%d-%m-%Y %H:%M:%S')}   '
#                 f'{self.text_article_or_news[:20]}')
#
#     def get_absolute_url(self):
#         return reverse('article_detail', args=[str(self.id)])
#
#
# # 4. Модель PostCategory
# # Промежуточная модель для связи «многие ко многим»:
# # связь «один ко многим» с моделью Post;
# # связь «один ко многим» с моделью Category.
# class PostCategory(models.Model):
#     post = models.ForeignKey('Post', on_delete = models.CASCADE)
#     category = models.ForeignKey('Category', on_delete = models.CASCADE)
#
#
# # 1. Модель Comment
# # Каждое объявление получает отклик.
# # Модель будет иметь следующие поля:
# # связь «один ко многим» с моделью Bulletin(Post);
# # связь «один ко многим» со встроенной моделью User
# # (комментарии может оставить любой пользователь, необязательно автор);
# # текст комментария;
# # дата и время создания комментария;
# # рейтинг комментария.
# class Comment(models.Model):
#     bulletin = models.ForeignKey('Bulletin', on_delete = models.CASCADE)
#     author = models.ForeignKey(User, on_delete = models.CASCADE)
#     text_comment = models.TextField()
#     date_and_time = models.DateTimeField(auto_now_add=True)
#     rating = models.IntegerField(default=0)
#
#     # Методы like() и dislike() увеличивают/уменьшают рейтинг на единицу.
#     def like(self):
#         self.rating += 1
#         self.save()
#
#     def dislike(self):
#         self.rating -= 1
#         self.save()
