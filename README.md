

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
    * A serializer implemented for the Property model in order to convert the response from the mocked HouseCanary server hosted locally via postman.
    * OAuth1 authentication configuration was used when sending requests to postman from this service.
    * A GetPropertyRequestSerializer to validate that the required fields (address and zipcode) are provided and not empty.
  
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
9. Make sure to grab the url from the postman mock server environment and replace the base url field in property_data_provider.api.urls.py
10. Spin up the Django server
   ```sh
   python manage.py runserver
   ``` 
11. Send the request from the Property data Provider Test Requests or go to http://127.0.0.1:8000/property_registration
12.  Additionally, some tests have be written in property_data_provider.tests.py which can be executed fro the root director where manage.py is via:
```sh
python manage.py test property_data_provider
```

## Closing Thoughts

While working with Django for the first time, I began to notice that, while it is very effective for integrating REST with a back end database server via models, it seemed a bit hacky leveraging the model object when mapping a third party api response.  For this reason, I may opt to Flask. In this solution I added some custom validation logic, but Flask has the reqparse module to do this for us saving some time and effort.

I may be bias but I of course have a preference for Java and Springboot because I have been using it significantly for the past few years.  I think it provides a robustness, which is sometimes viewed as a con due to the reliance on the spring framework, however it is very maintainable with its @annotations style.  What you may not get upfront in development agility, you make up with long term maintenance and durability whihc is why you see larger enterprise applications opting for this technology stack.

With that said python provides an extensive suite of modules/libraries enabling organizations to be quick to market with their applications.  Additionally, if there is potential for some data science/machine learning features to be integrated into the product, python is the way to go in my opinion.

## Future Steps

* Implement Multipage Frontend for the property registration, this registration could provide all the steps to filing for hometap services in a linear client experience based on the details of their home.
* Add some authentication across functional accounts/services (for example, limiting requests to only come from property_registration_facade).
* Design a more coherent and well flushed out api structure with standard error responses.