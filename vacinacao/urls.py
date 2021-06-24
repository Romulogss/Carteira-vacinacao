"""vacinacao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    delete_crianca,
    crianca_index,
    ciranca_create,
    crianca,
    vacinacao_delete,
    vacinacao_index
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crianca_index, name='index'),
    path('crianca', ciranca_create, name='crianca_create'),
    path('detail/<str:id>', crianca, name='detail'),
    path('delete/<str:id>', delete_crianca, name='crianca_delete'),
    path('vacinacao/<str:id>', vacinacao_index, name='vacinacao_index'),
    path('vacinacao/delete/<str:id>', vacinacao_delete, name='vacinacao_delete')
]
