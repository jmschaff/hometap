from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from property_registration_facade.forms import PropertyRegistrationForm, SepticPropertyRegistrationForm
from property_data_provider.serializers import PropertySerializer
from property_data_provider.models import Property


def property_registration(request):
    if request.method == 'POST':
        form = PropertyRegistrationForm(request.POST)
        if form.is_valid():
            URL = 'http://127.0.0.1:8000/property/'
            data = {
                'address': form.data['address'], 'zipcode': form.data['zipcode']}
            r = requests.get(url=URL, data=data)
            if r.status_code == 200:
                property = PropertySerializer(r.json())
                if property.data['sewer'] == 'septic':
                    return HttpResponseRedirect('septic_property_registration')
                else:
                    return HttpResponse("Thank you for registering your property!")
            elif r.status_code == 500:
                # Property not found in property_data_provider, default to not supportting region.
                return HttpResponse("We do not currently support the properties in your area :(")
    else:
        form = PropertyRegistrationForm()

    return render(request, 'propertyRegistrationForm.html', {'form': form})


def septic_property_registration(request):
    if request.method == 'POST':
        form = SepticPropertyRegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thank you for registering your property!")
    else:
        form = SepticPropertyRegistrationForm()

    return render(request, 'septicPropertyRegistrationForm.html', {'form': form})
