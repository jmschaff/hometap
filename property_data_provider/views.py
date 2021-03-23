from django.shortcuts import render
from rest_framework import views
from rest_framework import permissions
from property_data_provider.serializers import PropertySerializer
from property_data_provider.api.client import PropertyClient
from rest_framework.views import APIView
import json
from rest_framework.response import Response


class PropertyView(APIView):

    # TODO: Add authentication to ensure request is coming from functional service (property_registration_facade)

    def get(self, request):
        address = request.data["address"]
        zipcode = request.data["zipcode"]
        propertyClient = PropertyClient('v2')
        property = propertyClient.get_property_details(address, zipcode)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
