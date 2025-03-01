from django.contrib import admin
from .models import OrganizationProfile

@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
 list_display = ['user', 'registration_number', 'phone_number', 'regions_of_operation', 'compliance_status', 'registration_certificate', 'is_verified', 'website', 'annual_budget', 'registration_date', 'date_established']
 raw_id_fields = ['user']
