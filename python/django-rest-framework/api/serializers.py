from rest_framework import serializers
from .models.practitioner import (
    Practitioner,
    PractitionerAddress,
    PractitionerContactPoint,
    PractitionerIdentifier,
    PractitionerName,
    Qualification,
    QualificationIdentifier,
)


class PractitionerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractitionerAddress
        fields = "__all__"


class PractitionerContactPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractitionerContactPoint
        fields = "__all__"


class PractitionerIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractitionerIdentifier
        fields = "__all__"


class PractitionerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractitionerName
        fields = "__all__"


class QualificationIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationIdentifier
        fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

    qs = Qualification.objects.prefetch_related("identifiers")
    identifier = QualificationIdentifierSerializer(many=True)


class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = "__all__"

    qs = Practitioner.objects.prefetch_related(
        "addresses", "contact_points", "identifiers", "names", "qualifications"
    )
    identifiers = PractitionerIdentifierSerializer(many=True)
    names = PractitionerNameSerializer(many=True)
    contact_points = PractitionerContactPointSerializer(many=True)
    addresses = PractitionerAddressSerializer(many=True)
    qualifications = QualificationIdentifierSerializer(many=True)
