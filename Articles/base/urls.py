from django.urls import path
from .import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view

urlpatterns = [

    # Регистрация и авторизация
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Маршруты 
    path('', views.index, name='index'), # общий маршрут

    # Маршруты для авторов
    path('author_list/', views.author_list, name='author_list'),
    path('display_authors/', views.display_authors, name='display_authors'),
    path('add_author/', views.add_author, name='add_author'), 
    path('author/<int:pk>/', views.author_detail, name='author_detail'), 
    path('edit_author/<int:pk>/', views.edit_author, name='edit_author'), 
    path('delete_author/<int:pk>/', views.delete_author, name='delete_author'),  

    # Маршруты для статей
    path('article_list/', views.article_list, name='article_list'),
    path('display_articles/', views.display_articles, name='display_articles'),
    path('add_article/', views.add_article, name='add_article'),
    path('article/<int:pk>/detail/', views.article_detail, name='article_detail'),
    path('edit_article/<int:pk>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),    
]
