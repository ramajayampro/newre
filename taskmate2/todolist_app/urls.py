from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('view/<task_id>', views.view_task, name='view_task'), 
    path('complete', views.complete_task, name='complete_task'),
    path('finish', views.finish_task, name='finish_task'),
    path('finish1/<task_id>', views.finish1_task, name='finish1_task'),

]
