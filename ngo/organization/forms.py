# forms.py
from django import forms
from django.contrib.auth.models import User
from user_auth.models import OrganizationProfile

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


# class OrganizationEditForm(forms.ModelForm):
#   class Meta:
#     model = OrganizationProfile
#     fields = [
#       'phone_number',
#       'regions_of_operation',
#       'website',
#       'annual_budget',
#       'registration_date',
#       'date_established',
#       'registration_certificate'
#     ]
#     widgets = {
#       'regions_of_operation': forms.CheckboxSelectMultiple,
#       'registration_date': forms.DateInput(attrs={'type': 'date'}),
#       'date_established': forms.DateInput(attrs={'type': 'date'})
#     }


