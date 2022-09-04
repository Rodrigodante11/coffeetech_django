from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("coffeetech.urls")),
    path('login/', include("autenticacao.urls")),
    path('criar_contas/', include('contas.urls')),
]
