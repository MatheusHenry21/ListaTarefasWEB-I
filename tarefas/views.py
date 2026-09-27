from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarefa
from .forms import TarefaForm

class CriaTarefas(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = "adicionar.html"
    success_url = '/'

class ListaTarefas(ListView):
    model = Tarefa
    template_name = "index.html"
    context_object_name = 'tarefas'

    def get_queryset(self):
        self.queryset = Tarefa.objects.all()

        filtro = self.request.GET.get('filtro')

        if filtro == 'concluido':
            self.queryset = self.queryset.filter(concluido=True)

        elif filtro == 'pendente':
            self.queryset = self.queryset.filter(concluido=False)

        return self.queryset.order_by('nome')