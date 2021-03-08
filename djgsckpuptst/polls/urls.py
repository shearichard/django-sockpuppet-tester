from django.urls import path

from .views  import polls_increment
from . import viewsAvoidNameClash  as viewsANC

urlpatterns = [
    path('', viewsANC.index, name='index'),
    path('increment/', polls_increment.pollsincrement, name='increment'),
]


