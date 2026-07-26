from django.shortcuts import render
from .models import shipment

def shipment_list(request):
    envios = shipment.objects.all() # Trae todos los registros
    return render(request, 'shipments2/lista_shipments.html', {'envios': envios})

def shipment_detail(request, shipment_id):
    envio = shipment.objects.get(shipment_id=shipment_id) # Trae un registro específico
    return render(request, 'shipments2/detalle_envio.html', {'envio': envio})

from django.shortcuts import render, redirect, get_object_or_404
from .models import shipment

# ... tus vistas anteriores (shipment_list, etc.) ...

# 1. Eliminar Envío
def eliminar_shipment(request, shipment_id):
    envio = get_object_or_404(shipment, shipment_id=shipment_id)
    if request.method == 'POST':
        envio.delete()
        return redirect('shipment_list')
    return render(request, 'shipments2/confirmar_eliminar.html', {'envio': envio})

# 2. Redirección rápida al Admin para Crear y Editar 
# (Ideal si aún no creaste formularios HTML personalizados)
def nuevo_shipment(request):
    return redirect('/admin/shipments2/shipment/add/')

def editar_shipment(request, shipment_id):
    return redirect(f'/admin/shipments2/shipment/{shipment_id}/change/')
