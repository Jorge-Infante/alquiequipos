from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import OrderDetail, OrderDetailHistory

@receiver(post_save, sender=OrderDetail)
def actualizar_stock(sender, instance, **kwargs):
    if instance.equipment_delivered == None:
        print('es nuevo alquiler -----')
        service = instance.service
        service.stock -= instance.equipment_rented
        service.save()

@receiver(post_save, sender=OrderDetail)
def actualizar_precio_total(sender, instance, **kwargs):
    order = instance.order
    total = sum(detalle.service.unit_price * detalle.equipment_rented for detalle in order.orderdetail_set.all())
    order.total_price = total
    print('EL TOTAL EN EL SIGNAL: ',total)
    order.save()

@receiver(pre_save, sender=OrderDetail)
def create_order_detail_history(sender, instance, **kwargs):

    if instance.pk:
        original = OrderDetail.objects.get(pk=instance.pk)    
        print('Anterior : ',original, 'Instancia : ',instance)  
        OrderDetailHistory.objects.create(
            id_order = original.order.id,
            id_service = original.service.id,
            id_detail = original.id,
            detail_equipment_rented = original.equipment_rented,
            detail_equipment_delivered = original.equipment_delivered,
            detail_equipment_undelivered = original.equipment_undelivered,
            detail_created = original.created,
            detail_name = original.service.name
        )
        service = instance.service
        if(instance.equipment_undelivered == None):
            instance.equipment_undelivered = (instance.equipment_rented - instance.equipment_delivered)
            print('--- Instancia null --- ', instance.equipment_undelivered )
        else:
            instance.equipment_undelivered = (original.equipment_undelivered - instance.equipment_delivered)

        service.stock += instance.equipment_delivered
        service.save()
            
    else:
        instance.equipment_undelivered = instance.equipment_rented 

