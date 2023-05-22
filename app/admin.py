from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class PopularMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Display these fields in the change list
    search_fields = ('name',)  # Enable searching by name
    list_filter = ('price',)  # Enable filtering by price

admin.site.register(PopularMenu, PopularMenuAdmin)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'number_of_persons', 'date', 'time')
