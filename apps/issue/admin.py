from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('start_time',)
    
admin.site.register(Issue)