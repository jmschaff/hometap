from django.urls import path
from property_registration_facade import views

urlpatterns = [
    path("property_registration", views.property_registration,
         name="property_registration"),
    path("septic_property_registration", views.septic_property_registration,
         name="septic_property_registration"),
]
