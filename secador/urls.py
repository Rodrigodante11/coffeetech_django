from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('busca', views.buscar, name='buscar'),
    path('detail/<int:secador_id>', views.detail, name='detail'),
    path('excluir/<int:secador_id>', views.excluir, name='excluir'),

]
