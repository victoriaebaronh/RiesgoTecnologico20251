from django.db import models
import datetime

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=20, null=False)
	apellidop = models.CharField(max_length=20, null=False)
	correo = models.EmailField()
	contraseña = models.CharField(max_length=30, null=False)
	telefono = models.CharField(max_length=10)

class UserProfile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.nombre

    class Meta:
        verbose_name_plural=u'Perfiles de Usuario'

class Administrador(models.Model):
	nombre = models.CharField(max_length=350, null=False)
	apellidop = models.CharField(max_length=100, null=False)
	correo = models.CharField(max_length=50, null=False)
	contraseña = models.CharField(max_length=30, null=False)
	telefono = models.CharField(max_length=10)

class Anuncio(models.Model):
	tipo = models.CharField(max_length=350, null=False)
	zona = models.CharField(max_length=100, null=False)
	forma_pago = models.CharField(max_length=50, null=False)
	descripcion = models.CharField(max_length=350, null=False)
	imagen = models.ImageField(upload_to='djangouploads/files/covers')
	video = models.FileField(upload_to='videos_uploaded',null=True)
	contacto = models.CharField(max_length=100, null=False)
	vigencia = models.DateField(null=False)
	visibilidad = models.BooleanField(default=True)
	calificacion = models.DecimalField(max_digits=6, decimal_places=2)

class AnuncioContra(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
	fecha_contra = models.DateField(null=False)
	vigencia = models.DateField(null=False)
	calificacion = models.DecimalField(max_digits=6, decimal_places=2)