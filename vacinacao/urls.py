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
    crianca_index,
    crianca_create,
    crianca,
    crianca_update,
    delete_crianca,

    vacinacao_delete,
    vacinacao_index,

    vacina_index,
    vacina_create,
    vacina,
    delete_vacina,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', crianca_index, name='index'),
    path('crianca/create', crianca_create, name='crianca_create'),
    path('crianca/update/<str:id>', crianca_update, name='crianca_update'),
    path('crianca/delete/<str:id>', delete_crianca, name='crianca_delete'),

    path('vacinacao/<str:id>', vacinacao_index, name='vacinacao_index'),
    path('vacinacao/delete/<str:id>', vacinacao_delete, name='vacinacao_delete'),

    path('v', vacina_index, name='v_index'),
    path('vacina', vacina_create, name='vacina_create'),
    path('v_detail/<str:id>', vacina, name='v_detail'),
    path('v_delete/<str:id>', delete_vacina, name='vacina_delete'),
]
