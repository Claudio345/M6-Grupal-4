from django.contrib import admin
from . models import Categoria, Proveedor

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
class ProveedorAdmin(admin.ModelAdmin):
    exclude = ('create_at', )
    list_display = ('id', 'nombre', 'image', 'descuento', 'demora', 'create_at')
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)