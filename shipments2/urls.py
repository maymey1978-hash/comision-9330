from django.urls import path
from . import views

urlpatterns = [
    path('', views.shipment_list, name='shipment_list'),
    path('nuevo/', views.nuevo_shipment, name='nuevo_shipment'),
    path('editar/<int:shipment_id>/', views.editar_shipment, name='editar_shipment'),
    path('eliminar/<int:shipment_id>/', views.eliminar_shipment, name='eliminar_shipment'),
]