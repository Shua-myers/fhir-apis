from rest_framework import serializers
from .models.practitioner import Practitioner


class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = ["id", "active", "gender", "birth_date"]
