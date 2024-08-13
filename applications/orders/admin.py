from django.contrib import admin
from . models import Order,OrderDetail,OrderDetailHistory

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(OrderDetailHistory)

