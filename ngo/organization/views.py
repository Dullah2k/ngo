from django.http import HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_auth.models import OrganizationProfile
from organization.forms import OrganizationProfileForm, ProjectForm
from .models import Project

def dashboard(request):
  return render(request, 'organization/dashboard.html', {'section':'dashboard'})

def organization_list(request):
  organizations = OrganizationProfile.objects.select_related('user').all()
  
  context = {
    'section':'organization',
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
    'section':'organization',
    'org': organization,
    'compliance_status': dict(OrganizationProfile.ComplianceStatus.choices),
    'regions': dict(OrganizationProfile.Region.choices)
  }
  return render(request, 'organization/org_details.html', context)

def edit_organization(request, pk):
    organization = get_object_or_404(OrganizationProfile, pk=pk)
    
    # Authorization check
    if not (request.user == organization.user or request.user.is_staff):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = OrganizationProfileForm(
            request.POST, 
            request.FILES, 
            instance=organization,
            user=request.user
        )
        if form.is_valid():
            form.save()
            return redirect('organization:organization_detail', pk=pk)
    else:
        form = OrganizationProfileForm(instance=organization, user=request.user)
    
    context = {
        'section':'organization',
        'form': form,
        'org': organization,
        'region_choices': dict(OrganizationProfile.Region.choices),
        'compliance_status_choices': dict(OrganizationProfile.ComplianceStatus.choices)
    }
    return render(request, 'organization/org_edit.html', context)

@login_required
def create_project(request):
    organization = get_object_or_404(
        OrganizationProfile,
        user=request.user
    )
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.organization = request.user
            project.save()
            form.save_m2m()  # Save many-to-many data for target_regions
            messages.success(request, 'Project created successfully!')
            return redirect('organization:dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProjectForm()

    return render(request, 'organization/project/create.html', {
      'form': form,
      'organization': organization,
      'section':'project',
    })

@login_required
def project_list(request):
    projects = Project.objects.filter(
        organization=request.user
    ).order_by('-created_at')
    
    return render(request, 'organization/project/list.html', {
        'projects': projects,
        'section':'project',
        'status_choices': dict(Project.Status.choices),
        'funding_choices': dict(Project.FundingType.choices)
    })

def project_detail(request, pk):
    project = get_object_or_404(
        Project.objects.select_related('organization'),
        pk=pk
    )
    
    # Get related organization profile
    organization_profile = project.organization.organization_profile
    
    context = {
        'project': project,
        'section':'project',
        'organization': organization_profile,
        'status_choices': dict(Project.Status.choices),
        'funding_choices': dict(Project.FundingType.choices),
        'region_choices': dict(OrganizationProfile.Region.choices)
    }
    return render(request, 'organization/project/details.html', context)

