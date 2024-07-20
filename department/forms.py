from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'description', 'structure', 'work', 'in_events', 'FAQ', 'links']
        