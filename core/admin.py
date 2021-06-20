from django.contrib import admin
from .models import (
    Crianca,
    Vacina,
    Vacinacao
)
# Register your models here.
admin.site.register(Crianca)
admin.site.register(Vacina)
admin.site.register(Vacinacao)