from django.urls import path

from .views  import polls_increment
from . import viewsAvoidNameClash  as viewsANC

app_name = 'todo'
urlpatterns = [
    path('', viewsANC.index, name='index'),
    path('insert', viewsANC.insert_todo, name='insert'),
    path('delete/<int:todo_id>/', viewsANC.delete_todo, name='delete'),
    path('increment/', polls_increment.pollsincrement, name='increment'),
]


