from django.shortcuts import render, get_object_or_404
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

def organization_detail(request, pk):
  organization = get_object_or_404(
    OrganizationProfile.objects.select_related('user'),
    pk=pk
  )
  
  context = {
    'org': organization,
    'compliance_status': dict(OrganizationProfile.ComplianceStatus.choices),
    'regions': dict(OrganizationProfile.Region.choices)
  }
  return render(request, 'organization/org_details.html', context)