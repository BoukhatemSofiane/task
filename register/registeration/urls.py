from django.urls import path
from .views import register_super_admin, register_staff, register_customer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/super-admin/', register_super_admin, name='register_super_admin'),
    path('api/register/staff/', register_staff, name='register_staff'),
    path('api/register/customer/', register_customer, name='register_customer'),
]
