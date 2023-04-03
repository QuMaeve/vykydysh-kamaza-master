from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import tablib
import collections

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from django.apps import apps
from django.db import models

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserresourse(resources.ModelResource):
    # password = fields.Field(column_name='first_name', attribute='first_name',
    #                           widget=ForeignKeyWidget(CustomUser, 'first_name'))
    def init_instance(self,row=None):
        super(CustomUserresourse, self).__init__()
        # Получите все поля в модели Book под приложением таблиц, пожалуйста, измените таблицы в соответствии с вашим приложением
        field_list = apps.get_model('tables', 'CustomUser')._meta.fields
        self.vname_dict = {}
        self.fkey = []
        for i in field_list:
            print(i)
            self.vname_dict[i.name] = i.verbose_name    # Получить verbose_name всех полей и сохранить их в словаре
            if(isinstance(i, models.ForeignKey)):
                self.fkey.append(i.name)  

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        # make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        for row in dataset.dict:
            tmp = collections.OrderedDict()
            users = CustomUser.objects.all()
            for item in row:
                if item == 'password':
                    """
                    Вот ключ, найдите соответствующий идентификатор в таблице User по читаемому имени и добавьте его к импортированным данным.
                    """
                    print(item)
                    # tmp[item] = CustomUser.objects.get(username=row[item]).id
                else:
                    print(item)
                    # tmp[item] = row[item]
                    """
                         Ключевым моментом здесь является сравнение данных. Если данные совпадают, добавьте идентификатор, изначально указанный в таблице книги, к данным, которые необходимо импортировать.
                         Это не приведет к добавлению тех же данных, что и оригинал, аналогично методу create_or_update
                    """
            # for user in users:

            #     if row['name'] == user.name:
            #         tmp['id'] = user.id
            dict.append(tmp)
        dataset.dict = dict
        return dataset
    class Meta:
        model = CustomUser
        exclude =['id', 'password',]

class CustomUserAdmin(ImportExportActionModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = CustomUser
    resourse_class=CustomUserresourse
    list_display = (
        "username",
        "first_name","last_name","patronymic","email",
        "locality","classes","establishment","deleted",
        "is_staff", "is_active",
        )
    list_filter = (
        "groups__name",
        # "username","first_name","last_name","patronymic","email",
        "locality","classes","establishment",
        # "deleted",
        "is_staff", "is_active",
        )
    fieldsets = (
        (None, 
         {"fields": (
        "username","first_name","last_name",
        "patronymic","email","password",
        "locality","classes","establishment","deleted",
        )}
         ),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","first_name","last_name",
                "patronymic","email",
                "locality","classes","establishment","deleted",
                "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
