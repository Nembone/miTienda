from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'avalaible', 'creado', 'updated']
    list_filter = ['avalaible', 'creado', 'updated', 'category']
    list_editable = ['price', 'stock', 'avalaible']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)