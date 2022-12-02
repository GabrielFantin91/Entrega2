from django.urls import path
from AppCoder.views import *


urlpatterns = [

    path('area/',area, name="area"),
    path('',inicio, name="inicio"),
    path('encargados/',encargados, name= "encargados"),
    path('trabajadores/',trabajadores, name="trabajadores"),
    path('AreaFormulario/',area_formulario, name="AreaFormulario"),
    path('busqueda_area/',busqueda_area, name="busqueda_area"),
    path('buscar/',buscar, name="buscar"),
]