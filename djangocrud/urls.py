"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('Refrigerios/', views.index_shop, name='Refrigerios'),
    path('create_task/', views.ProductoForm, name='create_task'),


    path('productos/', views.listar_productos, name='listar_productos'),  
    path('productos/crear/', views.crear_producto, name='crear_producto'),  
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'), 
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

