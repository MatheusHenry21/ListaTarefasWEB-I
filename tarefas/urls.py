
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaTarefas.as_view(), name='home'),
    path('adicionar/', views.add, name='adicionar')
]
