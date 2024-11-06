# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from functools import wraps

def admin_only(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return render(request, 'access_denied.html')
    return _wrapped_view

@admin_only
@login_required
def create_employee(request):
    if request.method == 'POST':
        # Retrieve basic employee information from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        
        # Retrieve custom fields from the POST request
        custom_fields = {}
        for key in request.POST:
            if key.startswith('custom_field_'):
                field_name = key.split('_', 2)[-1]  # Extract custom field name
                custom_fields[field_name] = request.POST[key]
        
        # Create new employee
        employee = Employee.objects.create(
            name=name,
            email=email,
            position=position,
            custom_fields=custom_fields
        )
        return redirect('employee_detail', pk=employee.pk)
    
    return render(request, 'create_employee.html')

@admin_only
@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

@admin_only
@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        # Update basic employee information
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')

        # Update custom fields
        custom_fields = {}
        for key in request.POST:
            if key.startswith('custom_field_'):
                field_name = key.split('_', 2)[-1]  # Extract custom field name
                custom_fields[field_name] = request.POST[key]
        
        employee.custom_fields = custom_fields
        employee.save()
        return redirect('employee_detail', pk=employee.pk)

    return render(request, 'edit_employee.html', {'employee': employee})


@login_required
def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee_list.html', {'employees': employees})

@admin_only
@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request,'Employee deleted successfully')
        return redirect('employee_list')
    return redirect('employee_list')