from django.contrib import admin
from principal.models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id', 'nome')
    
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)