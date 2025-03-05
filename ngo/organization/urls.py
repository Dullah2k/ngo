from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = "organization"
urlpatterns = [
  path('dashboard/', views.dashboard, name="dashboard"),
  path('organizations/', views.organization_list, name='organization_list'),
  path('organizations/<int:pk>/', views.organization_detail, name='organization_detail'),
  path('organizations/<int:pk>/edit/', views.edit_organization, name='edit_organization'),

  path('organization/projects/create/', views.create_project, name='create_project'),
  path('organization/projects/list', views.project_list, name='project_list'),
  path('organization/projects/<int:pk>/', views.project_detail, name='project_detail'),

  path('organization/reports/create/', views.create_report, name='create_report'),
  path('organization/reports/', views.report_list, name='report_list'),
  # path('organization/reports/<int:pk>/', views.report_detail, name='report_detail'),
]