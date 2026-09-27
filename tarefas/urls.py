
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaTarefas.as_view(), name='listar'),
    path('adicionar/', views.CriaTarefas.as_view(), name='adicionar')
]
