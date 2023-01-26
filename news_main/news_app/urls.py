from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('news_insert/', views.news_insert, name='news_insert'),
    path('logout/', views.user_logout, name="logout"),
    path('categories/', views.add_categories, name="add_categories"),
    path('news_main/', views.news_main, name='news_main'),
    path('one_news/<slug:slug>', views.one_news, name="one_news"),
    path('edit/<slug:slug>', views.edit_news, name="edit_news"),
    path('delete/<slug:slug>', views.delete_news, name="delete_news")
]
