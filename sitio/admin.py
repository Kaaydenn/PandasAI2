from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio', 'stock', 'marca', 'categoria']
    list_editable = ['stock']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['categoria']

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito)
admin.site.register(Carrito_item)
admin.site.register(Order)
admin.site.register(Order_Detail)