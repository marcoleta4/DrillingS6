from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from .forms import InputForm, BoardsForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Auto
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http.response import JsonResponse

# Create your views here.
def is_staff(user):
    return user.is_staff

@login_required(login_url='/login')
@permission_required('vehiculo.visualizar_catalogo',  login_url='/')
def listarjs_view(request):
    return render(request, "listarjs.html")

def list_autos_view(request):
    print(request)
    autos = list(Auto.objects.values())
    data = {'autos': autos}
    return JsonResponse(data)

@login_required(login_url='/login')
@permission_required('vehiculo.visualizar_catalogo',  login_url='/')
def listar_view(request):
    autosListado = Auto.objects.all()

    return render(request, "listar.html", {"autos": autosListado})

@login_required(login_url='/login')
@user_passes_test(is_staff, login_url='/')
@permission_required('vehiculo.visualizar_catalogo',  login_url='/')
def add_view(request):
    autosListado = Auto.objects.all()
    return render(request, "add.html", {"autos": autosListado})

def registrarauto_view(request):
    if request.method == 'POST':
        marca = request.POST.get('selectMarca')
        modelo = request.POST.get('txtModelo')
        serialCarroceria = request.POST.get('txtSerialCarroceria')
        serialMotor = request.POST.get('txtSerialMotor')
        categoria = request.POST.get('selectCategoria')
        precio = request.POST.get('txtPrecio')
        fechaCreacion = datetime.now().strftime("%Y-%m-%d")  # Obtener fecha actual en formato YYYY-MM-DD

        auto = Auto(marca=marca, modelo=modelo, serialCarroceria=serialCarroceria,
                    serialMotor=serialMotor, categoria=categoria, precio=precio, fechaCreacion=fechaCreacion)
        auto.save()
    messages.success(request, '¡Automovil Registrado!')  
    return redirect('/add')

def edicionauto_view(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, "edicionauto.html", {"auto": auto})

def editarauto_view(request, id):
    auto = Auto.objects.get(id=id)

    if request.method == 'POST':
        # Obtener los valores del formulario
        marca = request.POST.get('selectMarca')
        modelo = request.POST.get('txtModelo')
        serialCarroceria = request.POST.get('txtSerialCarroceria')
        serialMotor = request.POST.get('txtSerialMotor')
        categoria = request.POST.get('selectCategoria')
        precio = request.POST.get('txtPrecio')

        # Actualizar los atributos del objeto Auto
        auto.marca = marca
        auto.modelo = modelo
        auto.serialCarroceria = serialCarroceria
        auto.serialMotor = serialMotor
        auto.categoria = categoria
        auto.precio = precio

        # Guardar los cambios en la base de datos
        auto.save()
        messages.success(request, '¡Automovil Editado!') 
        return redirect('/add/')  # Redirigir a la página principal
    return render(request, "add.html", {"auto": auto})

def eliminarauto_view(request, id):
    auto = get_object_or_404(Auto, id=id)  # Obtener el objeto Auto con el id especificado
    auto.delete()
    messages.success(request, '¡Automovil Eliminado!') 
    return redirect('/add')

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como : {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
    
        messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)

class Persona(object):
    def __init__(self, nombre, apellido, login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login

def index(request):
    return HttpResponse("Mensaje, Hola Mundo")

class IndexPageView(TemplateView):
    template_name = 'index.html'






