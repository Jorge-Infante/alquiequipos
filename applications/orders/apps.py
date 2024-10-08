from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.orders'

    def ready(self):
        import applications.orders.signals
