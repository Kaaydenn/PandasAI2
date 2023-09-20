from django import forms
from django.db.models import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

""" 
    PRODUCTO 
"""
class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('titulo','imagen','descripcion', 'marca', 'color', 'stock', 'precio', 'codigo', 'categoria')
        """ widgets = {
            'titulo': forms.TextInput(),
            'descripcion' : forms.Textarea(),
            'marca' : forms.TextInput(),
            'color' : forms.TextInput(),
            'stock': forms.NumberInput(),
            'precio' : forms.NumberInput(),
            'codigo' : forms.TextInput(),
            'imagen' : forms.FileField()
        } """
        """ widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del producto...' , 'required': True}),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control', 'row' : 3, 'required': True}),
            'marca' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la marca del producto...' , 'required': True}),
            'color' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el color del producto...' , 'required': True}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el stock del producto...' , 'required': True}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'XXXX', 'required': True}),
            'codigo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el codigo del producto...' , 'required': True}),
            'imagen' : forms.FileField(attrs={'class':'form-control-file', 'id':'imagen', 'placeholder': 'Ingrese la imagen...', 'required': True})
        } """

