from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import OrganizationRegistrationForm
from .models import OrganizationProfile

def organization_registration(request):
  if request.method == 'POST':
    form = OrganizationRegistrationForm(request.POST)
    if form.is_valid():
      try:
        # Create User
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Create Organization Profile
        OrganizationProfile.objects.create(
          user=user,
          registration_number=form.cleaned_data['registration_number'],
          phone_number=form.cleaned_data['phone_number'],
          regions_of_operation=form.cleaned_data['regions_of_operation']
        )

        # Auto-login & redirect
        login(request, user)
        messages.success(request, 'Registration successful! Complete your profile details After you have logged in.')
        return redirect('user_auth:login')
      
      except Exception as e:
        messages.error(request, f'Registration failed: {str(e)}')
    else:
      messages.error(request, 'Please correct the errors below.')
  else:
    form = OrganizationRegistrationForm()

  return render(request, 'registration/org_register.html', {
    'form': form,
    'region_choices': OrganizationProfile.Region.choices
  })