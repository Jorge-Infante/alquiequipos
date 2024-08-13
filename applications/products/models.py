from django.db import models

class Measure(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return 'Id: '+str(self.id)+' | Nombre: '+ self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return 'Id: '+str(self.id)+' | Nombre: '+self.name+' | Tamaño: '+str(self.size)+self.measure.name+ ' | Registradas en bodega: '+ str(self.quantity)

class Service(models.Model):
    name = models.CharField(max_length=100)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return 'Id :'+str(self.id)+' | Nombre: '+self.name+ ' | Disponibles: '+str(self.stock)+' | Precio unitario: '+ str(self.unit_price)



