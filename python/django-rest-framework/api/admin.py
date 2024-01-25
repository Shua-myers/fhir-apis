from django.contrib import admin
from .models.practitioner import (
    Practitioner,
    PractitionerAddress,
    PractitionerContactPoint,
    PractitionerName,
    PractitionerIdentifier,
)


admin.site.register(Practitioner)
admin.site.register(PractitionerAddress)
admin.site.register(PractitionerContactPoint)
admin.site.register(PractitionerName)
admin.site.register(PractitionerIdentifier)
