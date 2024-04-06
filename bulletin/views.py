from django.views.generic import ListView, CreateView
from .models import Bulletin
from .forms import BulletinForm

# Добавляем новое представление для ввода объявлений.
class BulletinCreate(CreateView):
    # Проверка доступа на добавление.
    permission_required = ('bulletin.add_bulletin',)
    form_class = BulletinForm
    model = Bulletin
    template_name = 'bulletin/bulletin_edit.html'


class BulletinList(ListView):
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

    # # Переопределяем функцию получения списка статей.
    # def get_queryset(self):
    #     # Получаем обычный запрос
    #     queryset = super().get_queryset()
    #     # Используем наш класс фильтрации.
    #     # self.request.GET содержит объект QueryDict, который мы рассматривали
    #     # в этом юните ранее.
    #     # Сохраняем нашу фильтрацию в объекте класса,
    #     # чтобы потом добавить в контекст и использовать в шаблоне.
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     # Возвращаем из функции отфильтрованный список статей
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Добавляем в контекст объект фильтрации.
    #     context['filterset'] = self.filterset
    #     return context
