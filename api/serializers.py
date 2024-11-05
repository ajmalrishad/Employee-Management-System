from rest_framework import serializers
from employee_app.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.
    Includes validation logic and ensures proper data handling.
    """

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']  # Example of read-only fields