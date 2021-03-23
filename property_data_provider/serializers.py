from property_data_provider.models import GetPropertyRequest, Property
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class GetPropertyRequestSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        errors = []
        if "address" not in attrs:
            errors.append(
                "Missing required field [address] from GetPropertyRequest.")
        elif attrs["address"] == "":
            errors.append(
                "Required field [address] cannot be empty in GetPropertyRequest.")
        if "zipcode" not in attrs:
            errors.append(
                "Missing required field [zipcode] from GetPropertyRequest.")
        elif attrs["zipcode"] == "":
            errors.append(
                "Required field [zipcode] cannot be empty in GetPropertyRequest.")
        if len(errors) > 0:
            raise ValidationError(errors)

    class Meta:
        model = GetPropertyRequest
        fields = '__all__'
