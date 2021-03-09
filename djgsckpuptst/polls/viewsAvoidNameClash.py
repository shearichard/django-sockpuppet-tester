from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Todo
from .models import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('title')
    import pprint
    pprint.pprint(todo_list)
    template = loader.get_template('todo/index.html')
    context = {
        'todo_list': todo_list,
    }
    return HttpResponse(template.render(context, request))

def insert_todo(request):
    if request.method == "POST":
        f = TodoForm(request.POST)
        if f.is_valid():
            todo_obj= Todo.objects.create(title=f.data['title'], description=f.data['description'])
            todo_obj.save()

        return redirect('/polls')
    else:
        template = loader.get_template('todo/detail.html')
        context = {}
        return HttpResponse(template.render(context, request))

def delete_todo(request, todo_id):
    query = Todo.objects.get(pk=todo_id)
    query.delete()
    return redirect('/polls')
