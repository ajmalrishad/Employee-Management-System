# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_employee, name='create_employee'),
    path('<int:pk>/', employee_detail, name='employee_detail'),
    path('<int:pk>/edit/', edit_employee, name='edit_employee'),
    path('employee_list', employee_list, name='employee_list'),
]
