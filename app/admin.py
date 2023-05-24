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


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__category_name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')