# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Set up router
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('v1/', include(router.urls)),  # Employee CRUD endpoints
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login endpoint
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh endpoint
]
