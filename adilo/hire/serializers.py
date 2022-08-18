from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models


class AddCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HireProcess
        fields = ["id", "name", "gender"]

    def validate_name(self, value):
        if value == "admin":
            raise ValidationError("someone is trying to break the system")
        return value


class ApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HireProcess
        fields = ["id", "name", "approved"]

    def validate_name(self, value):
        if value == "admin":
            raise ValidationError("someone is trying to break the system")
        return value
