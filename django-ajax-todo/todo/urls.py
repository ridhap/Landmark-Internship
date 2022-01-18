from django.urls import path

from . import views
app_Name='todo'
urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('todo-list/', views.todo_list, name='todo-list'), 
    path('todo-create/', views.todo_create, name='todo-create'),
    path('todo-edit/', views.todo_edit, name='todo-edit'),
    path('todo-delete/', views.todo_delete, name='todo-delete'),
]