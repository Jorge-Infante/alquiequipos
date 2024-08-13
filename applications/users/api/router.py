from django.urls import path
from rest_framework.routers import DefaultRouter
from applications.users.api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router_user = DefaultRouter()
router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)
router_user.register(
    prefix='groups', basename='groups', viewset=GroupViewSet
)
router_user.register(
    prefix='permisions', basename='permisions', viewset=PermissionViewSet
)

urlpatterns = [
    path('auth/me/', UserView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
