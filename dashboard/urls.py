from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('retorna_dados_dashboard', views.retorna_dados_dashboard, name='retorna_dados_dashboard'),
]
