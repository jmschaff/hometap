from django.test import TestCase
import pytest
import deepdiff
from property_data_provider.api.urls import URLs
from rest_framework.test import APIClient, APITestCase
import requests_mock
import json
import requests
from property_data_provider.serializers import PropertySerializer


class PropertyTests(APITestCase):

    @requests_mock.Mocker()
    def test_get_property_details_v2(self, requests_mock):

        address = "800 Boylston St"
        zipcode = "02199"
        urls = URLs('v2')

        requests_mock.get(urls.property_details_url(address, zipcode),
                          json={
            "api_code_description": "ok",
            "api_code": 0,
            "result": {
                "property": {
                    "air_conditioning": "yes",
                    "attic": False,
                    "basement": "none",
                    "building_area_sq_ft": 1824,
                    "building_condition_score": 5,
                    "building_quality_score": 3,
                    "construction_type": "Wood",
                    "exterior_walls": "wood_siding",
                    "fireplace": False,
                    "full_bath_count": 2,
                    "garage_parking_of_cars": 1,
                    "garage_type_parking": "underground_basement",
                    "heating": "forced_air_unit",
                    "heating_fuel_type": "gas",
                    "no_of_buildings": 1,
                    "no_of_stories": 2,
                    "number_of_bedrooms": 4,
                    "number_of_units": 1,
                    "partial_bath_count": 1,
                    "pool": True,
                    "property_type": "Single Family Residential",
                    "roof_cover": "Asphalt",
                    "roof_type": "Wood truss",
                    "site_area_acres": 0.119,
                    "style": "colonial",
                    "total_bath_count": 2.5,
                    "total_number_of_rooms": 7,
                    "sewer": "septic",
                    "subdivision": "CITY LAND ASSOCIATION",
                    "water": "septic",
                    "year_built": 1957,
                    "zoning": "RH1"
                },
                "assessment": {
                    "apn": "0000 -1111",
                    "assessment_year": 2015,
                    "tax_year": 2015,
                    "total_assessed_value": 1300000,
                    "tax_amount": 15199.86
                }
            }
        })
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps({"address": address,
                                                                                     "zipcode": zipcode}), content_type='application/json')
        respSerializer = PropertySerializer(resp.data)
        expectedSerializer = PropertySerializer({
            "air_conditioning": "yes",
            "attic": False,
            "basement": "none",
            "building_area_sq_ft": 1824,
            "building_condition_score": 5,
            "building_quality_score": 3,
            "construction_type": "Wood",
            "exterior_walls": "wood_siding",
            "fireplace": False,
            "full_bath_count": 2,
            "garage_parking_of_cars": 1,
            "garage_type_parking": "underground_basement",
            "heating": "forced_air_unit",
            "heating_fuel_type": "gas",
            "no_of_buildings": 1,
            "no_of_stories": 2,
            "number_of_bedrooms": 4,
            "number_of_units": 1,
            "partial_bath_count": 1,
            "pool": True,
            "property_type": "Single Family Residential",
            "roof_cover": "Asphalt",
            "roof_type": "Wood truss",
            "site_area_acres": 0.119,
            "style": "colonial",
            "total_bath_count": 2.5,
            "total_number_of_rooms": 7,
            "sewer": "septic",
            "subdivision": "CITY LAND ASSOCIATION",
            "water": "septic",
            "year_built": 1957,
            "zoning": "RH1"})

        assert respSerializer.data == expectedSerializer.data

    def test_invalid_property_request_missing_address(self):
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps(
            {"zipcode": "02114"}), content_type='application/json')
        assert resp.status_code == 500
        assert "Missing required field [address] from GetPropertyRequest." in resp.data['detail']

    def test_invalid_property_request_missing_empty_address(self):
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps(
            {"address": "", "zipcode": "02114"}), content_type='application/json')
        assert resp.status_code == 500
        assert "Required field [address] cannot be empty in GetPropertyRequest." in resp.data['detail']

    def test_invalid_property_request_missing_zipcode(self):
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps(
            {"address": "800 Boylston St"}), content_type='application/json')
        assert resp.status_code == 500
        assert "Missing required field [zipcode] from GetPropertyRequest." in resp.data['detail']

    def test_invalid_property_request_missing_empty_zipcode(self):
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps(
            {"address": "800 Boylston St", "zipcode": ""}), content_type='application/json')
        assert resp.status_code == 500
        assert "Required field [zipcode] cannot be empty in GetPropertyRequest." in resp.data['detail']

    @requests_mock.Mocker()
    def test_404_adpi_code_property_not_found(self, requests_mock):
        address = "800 Boylston St"
        zipcode = "02199"
        urls = URLs('v2')

        requests_mock.get(urls.property_details_url(address, zipcode),
                          json={
            "api_code_description": "property not found",
            "api_code": 404,
            "result": {}
        })
        resp = self.client.generic(method="GET", path="/property/", data=json.dumps({"address": address,
                                                                                     "zipcode": zipcode}), content_type='application/json')
        assert resp.status_code == 500
        assert "property not found" in resp.data['detail']
