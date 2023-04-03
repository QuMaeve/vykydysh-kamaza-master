from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    patronymic = models.CharField(max_length=150, null=True, blank=True)
    description =  models.TextField(max_length=500, null=True, blank=True)
    deleted = models.BooleanField(default=0)

    def __str__(self):
        # self.first_name = first_name
        # self.last_name = last_name
        # self.patronymic = patronymic
        return f"{self.first_name} {self.last_name} {self.patronymic}"
    class Meta:
         verbose_name = "Автор"
         verbose_name_plural = "Авторы"