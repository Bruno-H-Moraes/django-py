from django.contrib import admin
from .models import Produto, Cliente
# Register your models here.

# class ProdutoAdmin(admin.modelAdmin):
#     list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
 

admin.site.register(Produto)
admin.site.register(Cliente, ClienteAdmin)

