from django import template
register = template.Library()

@register.filter
def mascara_cpf(cpf):
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'