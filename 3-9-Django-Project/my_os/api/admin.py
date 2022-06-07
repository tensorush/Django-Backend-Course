from django.contrib import admin

from .models import System, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
