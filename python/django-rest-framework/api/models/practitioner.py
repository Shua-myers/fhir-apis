from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import Address, ContactPoint, HumanName, Identifier


class Practitioner(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        OTHER = "other", _("Other")
        UNKNOWN = "unknown", _("Unknown")

    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=Gender, default=Gender.UNKNOWN)
    birth_date = models.DateField(null=True)


class PractitionerAddress(Address):
    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.CASCADE, related_name="addresses"
    )


class PractitionerContactPoint(ContactPoint):
    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.CASCADE, related_name="contact_points"
    )


class PractitionerIdentifier(Identifier):
    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.CASCADE, related_name="identifiers"
    )


class PractitionerName(HumanName):
    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.CASCADE, related_name="names"
    )


class Qualification(models.Model):
    code = models.CharField(max_length=5)
    system = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    begin_effective_datetime = models.DateTimeField(auto_now_add=True)
    end_effective_datetime = models.DateTimeField(null=True)
    issuer = models.CharField(max_length=50, null=True)

    practitioner = models.ForeignKey(
        Practitioner, on_delete=models.CASCADE, related_name="qualifications"
    )


class QualificationIdentifier(Identifier):
    qualification = models.ForeignKey(
        Qualification, on_delete=models.CASCADE, related_name="identifiers"
    )
