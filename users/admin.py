from django.contrib import admin
from .models import Profile
from easy_select2 import select2_modelform

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = [
        'user',
        ('dob', 'gender'),
        ('weight', 'height'),
    ]
    list_display = ('user', 'gender', 'weight', 'height')
    list_filter = ('gender', )
    select2 = select2_modelform(Profile, attrs={'width': '250px'})
    form = select2