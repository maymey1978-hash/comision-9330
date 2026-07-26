from django.db import models

# Create your models here.
class shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    FECHAETA = models.CharField(max_length=100)
    CANTIDAD = models.DecimalField(max_digits=10, decimal_places=2)
    TOTAL = models.CharField(max_length=50)
    FECHADESPACHO = models.DateField()
    FECHAENTREGA = models.DateField()
    LOTENUM = models.CharField(max_length=50)
    VENCIMIENTO = models.DateField()
    NUMERODESPACHO = models.CharField(max_length=50)


    def __str__(self):
        return f"Shipment {self.shipment_id} from {self.producto} to {self.FECHAETA}"
        