from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    pass
    username = models.CharField("Хуилия", unique=True, blank=True, null=False, max_length=150)
    first_name = models.CharField("Фамилия", max_length=150, null=True, blank=True)
    last_name = models.CharField("Имя", max_length=150, null=True, blank=True)
    patronymic = models.CharField("Отчество", max_length=150, null=True, blank=True)
    email = models.CharField("Электронная почта", max_length=254, null=True, blank=True)
    
    classes =  models.ForeignKey(
        'studentclass.Class',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='user_classes',
        verbose_name="Класс",
    )
    locality =  models.ForeignKey(
        'locality.Locality',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='user_locality',
        verbose_name="Территориальное образование",
    )
    establishment =  models.ForeignKey(
        'establishment.Establishment',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='user_establishment',
        verbose_name="Учебное учреждение",
    )
    deleted = models.BooleanField(default=0)

    REQUIRED_FIELDS=['patronymic',]
    USERNAME_FIELD='username'

    # objects = CustomUserManager()

    # def __str__(self, first_name, last_name, patronymic):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.patronymic = patronymic
    #     return self
    def __str__(self):
        return self.username
