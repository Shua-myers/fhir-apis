import pytest

from collections.abc import Mapping
from typing import Any

from api.models.practitioner import Practitioner
from api.views import practitioner_list
from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APIRequestFactory


@pytest.fixture
def practitioner_message() -> dict[str, Any]:
    # https://hl7.org/fhir/R4/practitioner-example-f002-pv.json
    return {
        "resourceType": "Practitioner",
        "id": "f002",
        "identifier": [
            {
                "use": "official",
                "system": "urn:oid:2.16.528.1.1007.3.1",
                "value": "730291637",
            },
            {
                "use": "usual",
                "system": "urn:oid:2.16.840.1.113883.2.4.6.3",
                "value": "174BIP3JH438",
            },
        ],
        "name": [
            {
                "use": "official",
                "family": "Voigt",
                "given": ["Pieter"],
                "suffix": ["MD"],
            }
        ],
        "telecom": [
            {"system": "phone", "value": "0205569336", "use": "work"},
            {"system": "email", "value": "p.voigt@bmc.nl", "use": "work"},
            {"system": "fax", "value": "0205669382", "use": "work"},
        ],
        "address": [
            {
                "use": "work",
                "line": ["Galapagosweg 91"],
                "city": "Den Burg",
                "postalCode": "9105 PZ",
                "country": "NLD",
            }
        ],
        "gender": "male",
        "birthDate": "1979-04-29",
    }


@pytest.mark.xfail
@pytest.mark.django_db
def test_create(practitioner_message: Mapping[str, Any]):
    factory = APIRequestFactory()
    request = factory.post("/Practitioner/", practitioner_message, format="json")
    request.user = AnonymousUser()

    response = practitioner_list(request)
    assert response.status_code == 200
    assert Practitioner.objects.count() == 1

    practitioner = Practitioner.objects.first()

    assert practitioner.names.first().family == "Voigt"
    # field level asserts


@pytest.mark.django_db
def test_read():
    # GIVEN an existing Practitioner record with an ID
    practitioner = Practitioner.objects.create(birth_date="1990-11-10")

    # WHEN a Practitioner Read is done on that ID
    factory = APIRequestFactory()
    request = factory.get(f"/Practitioner/{practitioner.pk}")
    request.user = AnonymousUser()
    response = practitioner_list(request)

    # THEN we get a Practitioner record that has the stuff from that record
    assert response.status_code == 200
    assert Practitioner.objects.count() == 1


def test_update():
    pass
    # GIVEN an existing Practitioner record with an ID
    # WHEN a Practitioner Update is done on that field
    # THEN we get back the same thing that was sent


def test_delete():
    pass
    # GIVEN an existing Practitioner
    # WHEN a Practitioner Delete message is done on that Practitioner
    # THEN it no longer exists


@pytest.mark.django_db
def test_search():
    """Test that a Practitioner search request is successful"""

    # GIVEN multiple Practitioners
    Practitioner.objects.create(birth_date="1990-11-10")
    Practitioner.objects.create(birth_date="1995-11-10")

    # WHEN a Practitioner Search is done
    factory = APIRequestFactory()
    request = factory.get("/Practitioner/")
    request.user = AnonymousUser()
    response = practitioner_list(request)

    # THEN we get a search bundle back with those 2 practitioners
    assert response.status_code == 200
    assert Practitioner.objects.count() == 2
