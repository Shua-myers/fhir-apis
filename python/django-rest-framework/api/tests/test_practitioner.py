import pytest

from api.models.practitioner import Practitioner
from api.views import practitioner_list
from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APIRequestFactory


@pytest.mark.xfail
@pytest.mark.django_db
def test_create():
    factory = APIRequestFactory()
    request = factory.post("/Practitioner/", {"patient": "new idea"}, format="json")
    request.user = AnonymousUser()

    response = practitioner_list(request)
    assert response.status_code == 200
    assert Practitioner.objects.count() == 1
    # field level asserts


def test_read():
    pass
    # GIVEN an existing Practitioner record with an ID
    # WHEN a Practitioner Read is done on that ID
    # THEN we get a Practitioner record that has the stuff from that record


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


def test_search():
    pass
    # GIVEN multiple Practitioners
    # WHEN a Practitioner Search is done
    # THEN we get a search bundle back with those 2 practitioners
