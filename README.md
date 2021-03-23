

  <h3 align="center">Hometap Interview Exercise</h3>

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [HouseCanary - as API reference](https://api-docs.housecanary.com/#property-details)

### Solution Overview

To accomplish this exercise, I created a Django web project with two applications:
  
  * property_data_provider:
    * Implements API wrapper that currently only exposes a single endpoint to retrieve property details provided an ***address*** and ***zipcode***, based on the HouseCanary Api documentation.
    * A model.Model named Property was structured based on the response object from https://api-docs.housecanary.com/#property-details
    * A basic serializer implemented for the Property model in order to convert the response from the mocked HouseCanary server hosted locally via postman.
    * OAuth1 authentication configuration was used when sending requests to postman from this service.
    * Some basic request validation to ensure address and zip code were provided by the requstor with error handling and error details provided from the stack trace.
  
  * property_registration_facade (Out of scope of the exercise requirements but wanted to take the intiative to familiarize my self with the Django framework)
    * Implements two views:
      * Property Registration:
        * A basic form with address and zipcode.
        * On submit, call the property_data_provider endpoint to retrieve property details.
        * If sewer == 'septic', route to additional form with septic specific questions.
        * Else, registration complete.
        * If property could not be found, default to page that states property location is not currently supported.

Additonally, a mock server was spun up via postman with some examples that are stored in this repo under postman_responses.

### 

### Installation / Usage

1. Clone the repo
   ```sh
   git clone https://github.com/jmschaff/hometap.git
   ```
2. Create virtual env
   ```sh
   python3 -m venv .
   ```
3. Activate virtual env
   ```sh
   source venv/bin/activate
   ```
5. Install depedencies
   ```sh
   pip install -r requirements.txt
   ```
6. Import postman collection: https://www.getpostman.com/collections/fcae5e5e838effe63fe4
7. Start mock server from connection
8. In Postman Mock Server folder from the collection, modify the get_property_details example response from any of the json files from the postman_response folder in the repo.
9. Spin up the Django server
   ```sh
   python manage.py runserver
   ``` 
10. Send the request from the Property data Provider Test Requests or go to http://127.0.0.1:8000/property_registration
