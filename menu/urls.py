from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.get_menu, name="get_menu"),
    path('specialities/', views.specialities, name="specialities"),
]