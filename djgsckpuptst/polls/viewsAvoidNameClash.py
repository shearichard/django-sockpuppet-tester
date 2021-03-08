from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Todo

def index(request):
    todo_list = Todo.objects.order_by('title')
    import pprint
    pprint.pprint(todo_list)
    template = loader.get_template('todo/index.html')
    context = {
        'todo_list': todo_list,
    }
    return HttpResponse(template.render(context, request))
