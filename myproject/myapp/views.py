from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
## from .forms import *
from .models import *
from django.template.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from .forms import UploadForm
from .forms import UploadForm2

# Create your views here.

def indexAnuncio(request):
	anuncios= Anuncio.objects.all()
	contexto = { 'anuncios': anuncios}

	return render(request, 'anuncios.html', contexto)

def indexUsuario(request):
	usuarios= Usuario.objects.all()
	contexto = { 'usuarios': usuarios}

	return render(request, 'usuario.html', contexto)

def indexAdmin(request):
	admins = Administrador.objects.all()
	contexto = { 'admins': admins}

	return render(request, 'admins.html', contexto)

def indexHome(request):
	return render(request, 'home.html')

def indexIniciar(request):
	return render(request, 'iniciarSesion.html')

def correo(request):
	return render(request, 'correo.html')

def indexGestionar(request):
	anuncios= Anuncio.objects.all()
	contexto = { 'anuncios': anuncios}

	return render(request, 'gestionarCatalogo.html', contexto)

def indexConsultar(request):
	return render(request, 'consultarSolicitudes.html')

def indexPublicar(request):
	return render(request, 'publicarAnuncio.html')

#def upload(request):
#	if request.method == "POST":
#		form = UploadForm(request.POST, request.FILES)
#		print(request.FILES)
#		if form.is_valid():
#			form.save()
#		return HttpResponseRedirect("/anuncios/")
#	return render(request, "home.html", {'form' : UploadForm})

def upload2(request):
	if request.method == "POST":
		form = UploadForm2(request.POST, request.FILES)
		print(request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect("/anuncios/")
	return render(request, "publicarAnuncio.html", {'form' : UploadForm2})

def upload(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        args['form'] = form
        if form.is_valid(): 
            form.save()  # guardar el usuario en la base de datos si es válido
            username = form.cleaned_data['nombre']
            email = form.cleaned_data['correo']
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]            
            activation_key = hashlib.sha1((salt+email).encode('utf-8')).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Obtener el nombre de usuario
            user=Usuario.objects.get(nombre=username)

            # Crear el perfil del usuario                                                                                                                                 
            new_profile = UserProfile(user=user, activation_key=activation_key, 
                key_expires=key_expires)
            new_profile.save()

            # Enviar un email de confirmación
            email_subject = 'Account confirmation'
            email_body = "Hola %s, Gracias por registrarte. Para activar tu cuenta da clíck en este link en menos de 48 horas: http://localhost:8080/confirmar/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'andycancer1@gmail.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/correo/')
    else:
        args['form'] = UploadForm()

    return render(request, 'home.html', args)


def register_confirm(request, activation_key):
    # Verifica que el usuario ya está logeado
    if request.user.is_authenticated:
        HttpResponseRedirect('/home')

    # Verifica que el token de activación sea válido y sino retorna un 404
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    # verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
    if user_profile.key_expires < timezone.now():
        return render_to_response('/home/')
    # Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
    user = user_profile.user
    user.is_active = True
    user.save()
    return render(request, 'iniciarSesion.html')

