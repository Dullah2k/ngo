from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_auth.models import OrganizationProfile

def dashboard(request):
  return render(request, 'organization/dashboard.html')

def organization_list(request):
  organizations = OrganizationProfile.objects.select_related('user').all()
  
  context = {
    'organizations': organizations,
    'compliance_status_choices': dict(OrganizationProfile.ComplianceStatus.choices),
    'region_choices': dict(OrganizationProfile.Region.choices)
  }
  return render(request, 'organization/orgs_list.html', context)