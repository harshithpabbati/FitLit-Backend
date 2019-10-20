from django.contrib import admin
from .models import Log
from easy_select2 import select2_modelform

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    select2 = select2_modelform(Log, attrs={'width': '250px'})
    form = select2