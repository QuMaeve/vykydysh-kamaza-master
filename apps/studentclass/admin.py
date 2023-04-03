from django.contrib import admin
from .models import Class

class ClassAdmin(admin.ModelAdmin):
    list_filter = (
        "establishment__locality__name",
        "establishment__name",
        )
admin.site.register(Class, ClassAdmin)