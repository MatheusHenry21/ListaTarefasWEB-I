from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarefa

class ListaTarefas(ListView):
    model = Tarefa
    template_name = "index.html"
    context_object_name = 'tarefas'

def add(request: HttpRequest):
    return render(request, 'adicionar.html')