from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Bulletin, Category


# Форма для ввода объявлений (article/).
class BulletinForm(forms.ModelForm):

    # Первичные устаноки отдельных полей.
    title_bulletin = forms.CharField(label='Заголовок')
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    category_bulletin = forms.ModelChoiceField(queryset=Category.objects.all(),
                                               label='Категория',
                                               widget=forms.Select,
                                               initial=Category.objects.first(),
                                               to_field_name='name_of_category',
                                               )
    #author_bulletin = forms.CharField(initial="новость", widget=forms.HiddenInput())
    author_bulletin = forms.ModelChoiceField(queryset=User.objects.all(),
                                             label='Автор',
                                             initial=User.objects.first(),
                                             to_field_name='username',
                                             )
    #date_and_time_bulletin = forms.DateTimeField(label='Дата и время создания')
    #author_bulletin = forms.CharField(label='Автор', disabled=True)

    class Meta:
        model = Bulletin
        fields = [
            'title_bulletin',
            'content',
            'category_bulletin',
            'author_bulletin',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(BulletinForm, self).__init__(*args, **kwargs)
    #     if self.instance.author_bulletin:
    #         self.fields['author_bulletin'].initial = self.instance.author_bulletin.username