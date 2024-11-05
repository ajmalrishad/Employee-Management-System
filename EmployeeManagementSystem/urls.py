# EmployeeManagementSystem/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee_app.urls')),
    path('api/', include('api.urls')),
    # other URLs for your project
]