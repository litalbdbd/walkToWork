from django import forms

from core.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'city',
            'job',
        )
