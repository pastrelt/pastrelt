from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Bulletin, Category, Comment, News


# Форма для рассылки новостей.
class NewsForm(forms.ModelForm):
    # Первичные устаноки отдельных полей.
    category_news = forms.ModelChoiceField(queryset=Category.objects.all(),
                                               label='Категория',
                                               widget=forms.Select,
                                               initial=Category.objects.first(),
                                               to_field_name='id',
                                               )
    title_news = forms.CharField(label='Заголовок')
    text_news = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))

    class Meta:
        model = News
        fields = [
            'category_news',
            'title_news',
            'text_news',
        ]


# Форма для ввода комментарий.
class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email', None)  # Извлекаем email из параметров
        super(CommentForm, self).__init__(*args, **kwargs)

        if email:
            user = User.objects.get(email=email)
            # Присваиваем значение первичного ключа пользователя
            self.fields['author_comment'].initial = user.id

    bulletin_key = forms.ModelChoiceField(queryset=Bulletin.objects.all(),
                                          label='Заголовок объявления',
                                          widget=forms.Select,
                                          initial=Bulletin.objects.first(),
                                          to_field_name='id',
                                          )
    text_comment = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    author_comment = forms.ModelChoiceField(queryset=User.objects.all(),
                                             widget=forms.HiddenInput(),
                                             required=False,
                                             )
    acceptance_flag = forms.BooleanField(widget=forms.HiddenInput(),
                                         initial=False,
                                         required=False)  # значение по умолчанию - False(0)

    class Meta:
        model = Comment
        fields = [
            'bulletin_key',
            'text_comment',
            'author_comment',
            'acceptance_flag',
        ]


# Форма для ввода объявлений.
class BulletinForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        email = kwargs.pop('email', None)  # Извлекаем email из параметров
        super(BulletinForm, self).__init__(*args, **kwargs)

        if email:
            user = User.objects.get(email=email)
            # Присваиваем значение первичного ключа пользователя.
            self.fields['author_bulletin'].initial = user.id

    title_bulletin = forms.CharField(label='Заголовок')
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    category_bulletin = forms.ModelChoiceField(queryset=Category.objects.all(),
                                               label='Категория',
                                               widget=forms.Select,
                                               initial=Category.objects.first(),
                                               to_field_name='name_of_category',
                                               )
    author_bulletin = forms.ModelChoiceField(queryset=User.objects.all(),
                                             widget=forms.HiddenInput(),
                                             required=False,
                                             )


    class Meta:
        model = Bulletin
        fields = [
            'title_bulletin',
            'content',
            'category_bulletin',
            'author_bulletin',
        ]