from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, views_ajax, add_task_ajax, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('view-json/', show_json, name='show_json'),
    path('json/', views_ajax, name='views_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax'),
]