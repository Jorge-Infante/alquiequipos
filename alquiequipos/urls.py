from django.contrib import admin
from django.urls import path,re_path,include
from applications.users.api.router import router_user
from applications.products.api.router import router_product
from applications.orders.api.router import router_order
from applications.clients.api.router import router_client

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('applications.users.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_order.urls)),
    path('api/', include(router_client.urls))
]

