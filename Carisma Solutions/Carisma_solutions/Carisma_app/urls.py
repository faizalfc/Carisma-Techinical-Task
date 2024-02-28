from django.contrib import admin

from django.urls import path
from .views import *

urlpatterns = [
    path('', loademp, name="le"),
    path('ue/', upemp),
    path('de/', delemp),
    path('se/', seremp),
    path('lm/', last),

    path('ge/', getemp),
    path('upe/', updateemp),
    path('demp/', deleteemp),
    path('semp/', searchemp),
    path('last/', last_modify)
]