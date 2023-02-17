from django.urls import path

from . import views

app_name = "paperelix"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/producto/', views.producto, name="detalle"),
    path('<str:nombre>/categoria/', views.categoria, name="categoria"),

]