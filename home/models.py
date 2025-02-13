# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    department = models.CharField(max_length=255, null=True, blank=True)
    job_tittle = models.CharField(max_length=255, null=True, blank=True)
    job_id = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Organization(models.Model):

    #__Organization_FIELDS__
    full_name = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    image_logo = models.CharField(max_length=255, null=True, blank=True)

    #__Organization_FIELDS__END

    class Meta:
        verbose_name        = _("Organization")
        verbose_name_plural = _("Organization")


class Department(models.Model):

    #__Department_FIELDS__
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Section(models.Model):

    #__Section_FIELDS__
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    primary_email = models.CharField(max_length=255, null=True, blank=True)
    primary_phone = models.CharField(max_length=255, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    #__Section_FIELDS__END

    class Meta:
        verbose_name        = _("Section")
        verbose_name_plural = _("Section")



#__MODELS__END
