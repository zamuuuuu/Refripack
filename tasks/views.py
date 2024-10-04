from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, CartItem, Cart

# Create your views here.

def signup(request):
    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html', {"form": UserCreationForm()})
    
    else:
        print(request.POST)
        print('Obteniendo datos')

        # Instanciar el formulario con los datos enviados
        form = UserCreationForm(request.POST)

        # Verificar que las contraseñas coincidan y que el formulario sea válido
        if form.is_valid():
            try:
                # Crear el usuario
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()

                # Iniciar sesión automáticamente
                login(request, user)
                return redirect('tasks')  # Redirige a la página de tareas o donde prefieras
            except IntegrityError:
                # Si el usuario ya existe, muestra el error
                return render(request, 'signup.html', {
                    "form": form,
                    "error": "El nombre de usuario ya existe."
                })

        # Si las contraseñas no coinciden o hay otros errores en el formulario
        return render(request, 'signup.html', {
            "form": form,
            "error": "Revisa que todos los campos esten rellenados correctamente."
        })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

@login_required
# Listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

@login_required
# Actualizar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

@login_required
# Eliminar producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})
        
        login(request, user)
        return redirect('home')

   
def index_shop(request):
    return render(request, 'refrigerios/index_shop.html')










   
