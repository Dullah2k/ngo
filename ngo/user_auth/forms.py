from django import forms
from django.contrib.auth.models import User
from .models import OrganizationProfile

class OrganizationRegistrationForm(forms.ModelForm):
  password = forms.CharField(
    label='Password',
    widget=forms.PasswordInput,
    min_length=8,
    help_text="Minimum 8 characters"
  )

  password2 = forms.CharField(
    label='Repeat password',
    widget=forms.PasswordInput
  )

  registration_number = forms.CharField(
    label="NGO Registration Number",
    max_length=20
  )

  phone_number = forms.CharField(
    label="Phone Number",
    max_length=15,
    # validators=[RegexValidator(r'^\+255\d{9}$')]
  )

  regions_of_operation = forms.MultipleChoiceField(
    choices=OrganizationProfile.Region.choices,
    widget=forms.CheckboxSelectMultiple
  )

  class Meta:
    model = User
    fields = ['username', 'first_name', 'email']
    labels = {
      'first_name': 'Organization Name'
    }

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd.get('password2'):
      raise forms.ValidationError("Passwords don't match.")
    return cd['password2']

  def clean_registration_number(self):
    number = self.cleaned_data['registration_number']
    if OrganizationProfile.objects.filter(registration_number=number).exists():
      raise forms.ValidationError("This registration number is already in use.")
    return number