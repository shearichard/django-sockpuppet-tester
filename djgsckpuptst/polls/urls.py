from django.urls import path

from .views  import polls_increment
from . import viewsAvoidNameClash  as viewsANC

app_name = 'todo'
urlpatterns = [
    path('', viewsANC.index, name='index'),
    path('insert', viewsANC.insert, name='insert'),
    path('increment/', polls_increment.pollsincrement, name='increment'),
]


