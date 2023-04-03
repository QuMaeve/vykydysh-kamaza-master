from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(_("Логин"), 
                                unique=True, blank=True, null=False, 
                                max_length=150)
    first_name = models.CharField(_("Фамилия"), 
                                  max_length=150, null=True, 
                                  blank=True)
    last_name = models.CharField(_("Имя"), 
                                 max_length=150, null=True, 
                                 blank=True)
    patronymic = models.CharField(_("Отчество"), 
                                  max_length=150, null=True, 
                                  blank=True)
    email = models.EmailField(_("Электронная почта"), 
                              max_length=254, null=True, 
                              blank=True)
    
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
    USERNAME_FIELD="username"
    REQUIRED_FIELDS=[]

    # objects = CustomUserManager()

    # def __str__(self, first_name, last_name, patronymic):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.patronymic = patronymic
    #     return self
    def __str__(self):
        return f" {self.classes} - {self.username} "
