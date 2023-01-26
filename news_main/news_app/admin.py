from django.contrib import admin
from .models import Category, NewsPage
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat']


@admin.register(NewsPage)
class AdminNewsPage(admin.ModelAdmin):
    list_display = ['title', 'desc', 'date', 'cat_id', 'user_name', 'image']
