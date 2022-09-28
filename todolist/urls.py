from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    # path('xml/', show_xml, name='show_xml'),
    # path('json/', show_json, name='show_json'),
    # path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    # path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]