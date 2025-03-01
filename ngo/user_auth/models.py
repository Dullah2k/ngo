from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

class OrganizationProfile(models.Model):
  class ComplianceStatus(models.TextChoices):
    COMPLIANT = 'C', _('Fully Compliant')
    PENDING = 'P', _('Pending Review')
    NON_COMPLIANT = 'N', _('Non-Compliant')
    SUSPENDED = 'S', _('Suspended')

  class Region(models.TextChoices):
    DAR = 'DAR', _('Dar es Salaam')
    DSM = 'DSM', _('Dodoma')
    ARU = 'ARU', _('Arusha')
    MBY = 'MBY', _('Mbeya')
    MWA = 'MWA', _('Mwanza')
    ZNZ = 'ZNZ', _('Zanzibar')
    KIG = 'KIG', _('Kigoma')
    TAN = 'TAN', _('Tanga')

  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='organization_profile'
  )
  
  # Registration required fields
  registration_number = models.CharField(
    _("NGO Registration Number"),
    max_length=20,
    unique=True,
    help_text=_("Official registration number from NGO Coordination Board")
  )

  phone_number = models.CharField(
    _("Phone Number"),
    max_length=15,
    validators=[RegexValidator(r'^\+255\d{9}$')]
  )

  regions_of_operation = ArrayField(
    models.CharField(max_length=3, choices=Region.choices),
    verbose_name=_("Regions of Operation")
  )

  # Optional fields
  compliance_status = models.CharField(
    _("Compliance Status"),
    max_length=1,
    choices=ComplianceStatus.choices,
    default=ComplianceStatus.PENDING
  )

  registration_certificate = models.FileField(
    _("Registration Certificate"),
    upload_to='ngo_docs/',
    blank=True
  )

  is_verified = models.BooleanField(default=False)

  website = models.URLField(_("Website"), blank=True)

  annual_budget = models.DecimalField(
    _("Annual Budget (TZS)"),
    max_digits=14,
    decimal_places=2,
    validators=[MinValueValidator(0)],
    null=True,
    blank=True
  )

  registration_date = models.DateField(
    _("Registration Date"),
    null=True,
    blank=True
  )

  date_established = models.DateField(
    _("Date Established"),
    null=True,
    blank=True
  )

  def __str__(self):
    return f'Profile of {self.user.username}'
