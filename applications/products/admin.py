from django.contrib import admin
from .models import Product,Service,Measure
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Measure)
# Register your models here.