from property_data_provider.models import GetPropertyRequest, Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class GetPropertyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetPropertyRequest
        fields = '__all__'
