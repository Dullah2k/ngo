from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField
from user_auth.models import OrganizationProfile
from django.conf import settings

class Project(models.Model):
  class Status(models.TextChoices):
    PLANNING = 'PLAN', _('Planning')
    ONGOING = 'ONGO', _('Ongoing')
    COMPLETED = 'COMP', _('Completed')
    SUSPENDED = 'SUSP', _('Suspended')

  class FundingType(models.TextChoices):
    GRANT = 'GRANT', _('Grant')
    DONATION = 'DON', _('Donation')
    SELF_FUNDED = 'SELF', _('Self-Funded')
    PARTNERSHIP = 'PART', _('Partnership')

  # Basic Information
  name = models.CharField(_("Project Name"), max_length=255)
  description = models.TextField(_("Project Description"))
  organization = models.ForeignKey(settings.AUTH_USER_MODEL,
      related_name='projects',
      on_delete=models.CASCADE)

  # Project Details
  start_date = models.DateField(_("Start Date"))
  end_date = models.DateField(_("End Date"), blank=True, null=True)
  status = models.CharField(
    _("Project Status"),
    max_length=4,
    choices=Status.choices,
    default=Status.PLANNING
  )

  funding_type = models.CharField(
    _("Funding Type"),
    max_length=5,
    choices=FundingType.choices,
    default=FundingType.GRANT
  )

  budget = models.DecimalField(
    _("Project Budget (TZS)"),
    max_digits=14,
    decimal_places=2,
    validators=[MinValueValidator(0)],
    blank=True,
    null=True
  )

  # Location and Beneficiaries
  target_regions = ArrayField(
    models.CharField(max_length=3, choices=OrganizationProfile.Region.choices),
    verbose_name=_("Target Regions"),
    blank=True,
    default=list
  )

  beneficiaries = models.PositiveIntegerField(
    _("Number of Beneficiaries"),
    blank=True,
    null=True
  )

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
      verbose_name = _("Project")
      verbose_name_plural = _("Projects")
      ordering = ['-created_at']
      indexes = [
        models.Index(fields=['status']),
        models.Index(fields=['organization']),
      ]

  def __str__(self):
      try:
          return f"{self.organization.organization_profile.registration_number} - {self.get_quarter_display()} {self.year}"
      except AttributeError:
          return f"Report {self.id}"

  def is_active(self):
    return self.status == self.Status.ONGOING

class Report(models.Model):
    QUARTER_CHOICES = [
        (1, 'Q1 - January to March'),
        (2, 'Q2 - April to June'),
        (3, 'Q3 - July to September'),
        (4, 'Q4 - October to December'),
    ]

    organization = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    projects = models.ManyToManyField('Project', related_name='reports')
    quarter = models.PositiveSmallIntegerField(choices=QUARTER_CHOICES)
    year = models.PositiveIntegerField()
    women_reached = models.PositiveIntegerField(default=0)
    men_reached = models.PositiveIntegerField(default=0)
    youth_reached = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('organization', 'quarter', 'year')
        ordering = ['-year', '-quarter']

    def __str__(self):
        return f"{self.organization.first_name} - {self.get_quarter_display()} {self.year}"

    def total_reached(self):
        return self.women_reached + self.men_reached + self.youth_reached