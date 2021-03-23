from requests_oauthlib import OAuth1
import datetime
import requests
import json
from property_data_provider.api.urls import URLs
from rest_framework.exceptions import APIException
from . import OAUTH_TOKEN, OAUTH_SECRET, CLIENT_KEY, CLIENT_SECRET


class PropertyClient:
    def __init__(self, version):
        self.url = URLs(version)

        self.oauth_secret = OAUTH_SECRET
        self.oauth_token = OAUTH_TOKEN
        self.client_key = CLIENT_KEY
        self.client_secret = CLIENT_SECRET

        self.auth_time = None
        self.auth = None
        self.valid_auth_dt = datetime.timedelta(seconds=10)

    def __create_auth(self):
        now = datetime.datetime.now()

        if self.auth == None or self.auth_time + self.valid_auth_dt < now:
            self.auth_time = now
            self.auth = OAuth1(self.client_key, self.client_secret, self.oauth_token,
                               self.oauth_secret, signature_type='auth_header')

    def __get_data(self, url):
        print(url)
        self.__create_auth()
        r = requests.get(url, auth=self.auth)
        response = r.json()
        if (self.__has_errors(response)):
            raise APIException(self.__get_error(response))
        else:
            return self.__get_result(response)

    def __has_errors(self, response):
        return response['api_code'] > 0

    def __get_error(self, response):
        return response['api_code_description']

    def __get_result(self, response):
        return response['result']

    def get_property_details(self, address, zipcode):
        return self.__get_data(self.url.property_details_url(address, zipcode))["property"]
