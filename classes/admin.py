from django.contrib import admin
from .models import Class

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'start_time', 'duration', 'location',
                    'price', 'deposit', 'image')
    list_filter = ('start_date', 'location')

admin.site.register(Class, ClassAdmin)
