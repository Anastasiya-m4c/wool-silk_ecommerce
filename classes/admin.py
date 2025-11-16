from django.contrib import admin
from django.utils.html import format_html
from .models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'start_date', 'start_time',
        'duration', 'location', 'price',
        'max_capacity', 'get_total_bookings_display',
        'get_spots_remaining_display', 'manually_fully_booked'
    )
    list_filter = ('start_date', 'location', 'manually_fully_booked')
    list_editable = ('manually_fully_booked',)
    
    def get_total_bookings_display(self, obj):
        """Display total bookings"""
        return obj.get_total_bookings()
    get_total_bookings_display.short_description = 'Booked'
    
    def get_spots_remaining_display(self, obj):
        """Display spots remaining with color coding"""
        spots = obj.get_spots_remaining()
        if obj.manually_fully_booked:
            color = 'red'
            text = '0 (Manual)'
        elif spots <= 0:
            color = 'red'
            text = '0'
        elif spots <= 3:
            color = 'orange'
            text = str(spots)
        else:
            color = 'green'
            text = str(spots)
        
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color, text
        )
    get_spots_remaining_display.short_description = 'Remaining'


admin.site.register(Class, ClassAdmin)