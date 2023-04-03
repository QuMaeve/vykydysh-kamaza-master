from django.contrib import admin
from .models import Establishment

class EstablishmentAdmin(admin.ModelAdmin):
    list_filter = (
        "locality__name",
        )
admin.site.register(Establishment,EstablishmentAdmin)