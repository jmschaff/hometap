class URLs():
    def __init__(self, version):

        # From postman mock server, this can always be modified to whatever the current vendor endpoint is
        self.base_url = 'https://f272640f-dbb6-4e62-96a9-79bc8245f4c1.mock.pstmn.io/'
        self.version = version
        self.property_details = '/property/details?address={}&zipcode={}'

    def property_details_url(self, address, zipcode):
        return self.base_url + self.version + self.property_details.format(address, zipcode)
