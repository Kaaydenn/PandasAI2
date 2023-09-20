from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    # Imagen
    imagen = models.FileField(upload_to='imagenes/productos/')
    descripcion = models.TextField(null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, default='')
    color = models.CharField(max_length=50, null=False, default='')
    precio = models.IntegerField(null=False, default=0)
    codigo = models.CharField(max_length=50, null=False, default='')
    stock = models.IntegerField(null=False, default=0)
    # FK
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return self.titulo

class Order(models.Model):
    ordernum = models.CharField(max_length=9, null=True, blank=True)
    customer = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.ordernum

class Order_Detail(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.titulo

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")
    total = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Usuario_id: {self.usuario.id} | Usuario: {self.usuario.username} | Total: {self.total}"


class Carrito_item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return f"Id: {self.pk} | Producto: {self.producto.titulo} | Carrito_id: {self.carrito.id}"