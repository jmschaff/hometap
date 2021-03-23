from django.shortcuts import render
from rest_framework import views
from rest_framework import permissions
from property_data_provider.serializers import GetPropertyRequestSerializer, PropertySerializer
from property_data_provider.api.client import PropertyClient
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import APIException
import traceback
import sys


class PropertyView(APIView):

    # TODO: Add authentication to ensure request is coming from functional service (property_registration_facade)

    def get(self, request):
        try:
            if "address" in request.data:
                address = request.data["address"]
            else:
                raise ValidationError(
                    "Missing address field from request body.")
            if "zipcode" in request.data:
                zipcode = request.data["zipcode"]
            else:
                raise ValidationError(
                    "Missing zipcode field from request body.")
            propertyClient = PropertyClient('v2')
            property = propertyClient.get_property_details(address, zipcode)
            serializer = PropertySerializer(property)
            return Response(serializer.data)
        except ValidationError:
            raise APIException(sys.exc_info())
