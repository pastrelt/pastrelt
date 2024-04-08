
from django.db import models

# БД для временного хранения данных при реистрации (почта и код).
class Registration(models.Model):
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=6)