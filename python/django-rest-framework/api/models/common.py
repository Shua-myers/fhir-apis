from django.db import models
from django.utils.translation import gettext_lazy as _


class StandardDatesMixin(models.Model):
    """
    Mixin to apply standard date fields to certain models.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True)
    begin_effective_datetime = models.DateTimeField(auto_now_add=True)
    end_effective_datetime = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Address(StandardDatesMixin):
    class AddressUse(models.TextChoices):
        HOME = "home", _("Home")
        WORK = "work", _("Work")
        TEMP = "temp", _("Temp")
        OLD = "old", _("Old")
        BILLING = "billing", _("Billing")

    class AddressType(models.TextChoices):
        POSTAL = "postal", _("Postal")
        PHYSICAL = "physical", _("Physical")
        BOTH = "both", _("Both")

    use = models.CharField(max_length=10, choices=AddressUse)
    address_type = models.CharField(
        max_length=10, choices=AddressType, default=AddressType.BOTH
    )
    text = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)


class ContactPoint(StandardDatesMixin):
    class ContactPointSystem(models.TextChoices):
        PHONE = "phone", _("Phone")
        FAX = "fax", _("Fax")
        EMAIL = "email", _("Email")
        PAGER = "pager", _("Pager")
        URL = "url", _("URL")
        SMS = "sms", _("SMS")
        OTHER = "other", _("Other")

    class ContactPointUse(models.TextChoices):
        HOME = "home", _("Home")
        WORK = "work", _("Work")
        TEMP = "temp", _("Temp")
        OLD = "old", _("Old")
        MOBILE = "mobile", _("Mobile")

    system = models.CharField(
        max_length=10, choices=ContactPointSystem, default=ContactPointSystem.OTHER
    )
    value = models.CharField(max_length=100)
    use = models.CharField(max_length=10)
    rank = models.PositiveSmallIntegerField()


class HumanName(StandardDatesMixin):
    class NameUse(models.TextChoices):
        USUAL = "usual", _("Usual")
        OFFICIAL = "official", _("Official")
        TEMP = "temp", _("Temp")
        NICKNAME = "nickname", _("Nickname")
        ANONYMOUS = "anonymous", _("Anonymous")
        OLD = "old", _("Old")
        MAIDEN = "maiden", _("Maiden")

    use = models.CharField(max_length=20, choices=NameUse, default=NameUse.USUAL)
    text = models.CharField(max_length=100)
    family = models.CharField(max_length=50)
    given = models.CharField(max_length=100)
    prefix = models.CharField(max_length=50)
    suffix = models.CharField(max_length=50)


class Identifier(StandardDatesMixin):
    class IdentifierUse(models.TextChoices):
        USUAL = "usual", _("Usual")
        OFFICIAL = "official", _("Official")
        TEMP = "temp", _("Temp")
        SECONDARY = "secondary", _("Secondary")
        OLD = "old", _("Old")

    use = models.CharField(
        max_length=20, choices=IdentifierUse, default=IdentifierUse.USUAL
    )
    type_code = models.CharField(max_length=5)
    type_system = models.CharField(max_length=50)
    type_display = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    assigner = models.CharField(max_length=50)
