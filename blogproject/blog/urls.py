from django.urls import path
from . import views



urlpatterns = [

    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create', views.create, name='create'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>', views.delete, name='delete'),

    path('comment_add/<int:blog_id>', views.comment_add, name='comment_add'),


] 