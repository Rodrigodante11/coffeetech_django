from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("coffeetech.urls")),
    path('contas/', include("autenticacao.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('criar_contas/', include('contas.urls')),
    path('accounts/', include('allauth.urls')),
    path('secador/', include('secador.urls')),
]
