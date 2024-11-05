# EmployeeManagementSystem/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('employee/', include('employee_app.urls')),
    # other URLs for your project
]