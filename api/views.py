from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from employee_app .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import action

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access
    
    
    def list(self, request, *args, **kwargs):
        """Handles listing all employees."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Employee list fetched successfully',
            'data': serializer.data
        })

    def retrieve(self, request, *args, **kwargs):
        """Handles fetching a single employee by ID."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'message': 'Employee details fetched successfully',
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        """Handles creating a new employee with custom response messages."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Employee created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Update an employee instance.
        """
        partial = kwargs.pop('partial', True)  # Allow partial updates
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Employee updated successfully.',
            'employee': serializer.data
        }, status=status.HTTP_200_OK)
        
    def destroy(self, request, *args, **kwargs):
        """Handles deleting an employee with a custom response message."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Employee deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

