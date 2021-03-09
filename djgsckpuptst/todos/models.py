# todos/models.py
from django.db import models
from django import forms

class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title

class TodoForm(forms.Form):
    class Meta:
        model = Todo 
        fields = ['title', 'description', 'completed']
