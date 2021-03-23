from django.urls import path

from .views import PropertyView


app_name = "property_data_provider"

urlpatterns = [
    path('property/', PropertyView.as_view()),
]
