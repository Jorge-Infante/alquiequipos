from django.db import models
from applications.products.models import Service
from django.utils import timezone


class Order(models.Model):
    services = models.ManyToManyField(Service, through='OrderDetail')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        services_name = [service.name for service in self.services.all()]
        services_str = ', '.join(services_name)
        return 'Id : '+ str(self.id)+' | Services: '+services_str+ ' |  Total orden $: '+str(self.total_price)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    equipment_rented = models.PositiveIntegerField()
    equipment_delivered = models.PositiveIntegerField(blank=True, null=True)
    equipment_undelivered = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ' Orden : '+str(self.order.id)+ ' | Servicio: '+ self.service.name +' | Cantidad: '+str(self.equipment_rented)+ ' | Precio unitario: '+str(self.service.unit_price)+ ' | Entregados: '+str(self.equipment_delivered)+ ' | En alquiler: '+str(self.equipment_undelivered)


class OrderDetailHistory(models.Model):
    id_order = models.PositiveIntegerField()
    id_service = models.PositiveIntegerField()
    id_detail = models.PositiveIntegerField()
    detail_name = models.CharField(max_length=100)
    detail_equipment_rented = models.PositiveIntegerField()
    detail_equipment_delivered = models.PositiveIntegerField(blank=True, null=True)
    detail_equipment_undelivered = models.PositiveIntegerField(blank=True, null=True)
    detail_created = models.DateTimeField()
    date_change = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return 'Orden: '+str(self.id_order)+' - Name: '+self.detail_name+' - Servicio: '+str(self.id_service)+' - Rentado:'+str(self.detail_equipment_rented)+' - Entregado:'+str(self.detail_equipment_delivered)+ ' - En alquiler: '+str(self.detail_equipment_undelivered)
    