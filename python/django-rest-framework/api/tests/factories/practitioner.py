import factory
from faker import Faker
from datetime import datetime

from api.models.practitioner import (
    Practitioner,
    PractitionerAddress,
    PractitionerContactPoint,
    PractitionerIdentifier,
    PractitionerName,
)

fake = Faker("en_US")


class PractitionerAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PractitionerAddress

    use = fake.enum(PractitionerAddress.AddressUse)
    address_type = fake.enum(PractitionerAddress.AddressType)
    line1 = fake.street_address()
    line2 = fake.secondary_address() if fake.pybool() else None
    city = fake.city()
    district = fake.text(max_nb_chars=50) if fake.pybool() else None
    state = fake.state()
    postal_code = fake.postalcode()
    country = fake.country()


class PractitionerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Practitioner

    birth_date = fake.date_of_birth()
    gender = fake.enum(Practitioner.Gender)
    address = factory.RelatedFactory(
        PractitionerAddressFactory, factory_related_name="practitioner"
    )


# PractitionerContactPointFactory
# PractitionerIdentifierFactory
# PractitionerNameFactory
# QualificationFactory
# QualificationIdentifierFactory

# TODO: add factories and fakers for the rest of the models
# test, but also verify in UI
