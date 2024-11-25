from django import forms
from django.forms import ModelForm
from .models import Usuario
from .models import Anuncio

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra
def save(self, commit=True):        
    user = super(UploadForm, self).save(commit=False)
    user.correo = self.cleaned_data['correo']
    if commit:
        user.is_active = False # No está activo hasta que active el vínculo de verificación
        user.save()
    return user

class UploadForm(ModelForm):
    nombre = forms.TextInput()
    apellidop = forms.TextInput()
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    contraseña = forms.TextInput()
    telefono = forms.TextInput()
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidop', 'correo', 'contraseña', 'telefono']

TIPO_CHOICES =(
    ('Albañil', "Albañil"),
    ("Carpinteria", "Carpinteria"),
    ("Herreria", "Herreria"),
    ("Plomeria", "Plomeria"),
    ("electrico", "Servicio electrico"),
    ("Otro", "Otro"),
)

ZONA_CHOICES =(
    ("Norte", "Norte"),
    ("Sur", "Sur"),
    ("Este", "Este"),
    ("Oeste", "Oeste"),
    ("Centro", "Centro"),
)

PAGO_CHOICES =(
    ("Efectivo", "Efectivo"),
    ("Tarjeta", "Tarjeta"),
    ("Transferencia", "Transferencia"),
)

class UploadForm2(ModelForm):
    tipo = forms.MultipleChoiceField(choices = TIPO_CHOICES)
    zona = forms.MultipleChoiceField(choices = ZONA_CHOICES)
    forma_pago = forms.MultipleChoiceField(choices = PAGO_CHOICES)
    descripcion = forms.TextInput()
    imagen = forms.ImageField()
    video = forms.TextInput()
    contacto = forms.TextInput()
    vigencia = forms.DateField()
    class Meta:
        model = Anuncio
        fields = ['tipo', 'zona', 'forma_pago', 'descripcion', 'imagen', 'video', 'contacto', 'vigencia']
            