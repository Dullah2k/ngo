# forms.py
from django import forms
from django.contrib.auth.models import User
from user_auth.models import OrganizationProfile
from django.utils import timezone
from .models import Project


class OrganizationProfileForm(forms.ModelForm):
    regions_of_operation = forms.MultipleChoiceField(
        choices=OrganizationProfile.Region.choices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = OrganizationProfile
        exclude = ['user', 'registration_number']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'date_established': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'pattern': '\+255\d{9}'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if not self.user.is_staff:
            admin_fields = ['compliance_status', 'is_verified']
            for field in admin_fields:
                if field in self.fields:
                    del self.fields[field]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'start_date',
            'end_date',
            'status',
            'funding_type',
            'budget',
            'target_regions',
            'beneficiaries'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'target_regions': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        
        if end_date and start_date and end_date < start_date:
            raise forms.ValidationError("End date cannot be before the start date.")
        return end_date


