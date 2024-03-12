from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       # особенное значение ’__all__’, которое означает, что Django сам должен пойти в модель и взять все поля,
       # кроме первичного ключа
       fields = '__all__'

# class ProductForm(forms.ModelForm):
#    class Meta:
#        model = Product
#        fields = [
#            'name',
#            'description',
#            'quantity',
#            'category',
#            'price',
#        ]