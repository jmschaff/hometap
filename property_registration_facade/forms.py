from django import forms


class PropertyRegistrationForm(forms.Form):
    address = forms.CharField(label='Street address', max_length=100)
    zipcode = forms.CharField(label='Zip code', max_length=100)


class SepticPropertyRegistrationForm(forms.Form):
    location_of_septic_system = forms.CharField(
        label='Location of septic system', max_length=100)
    installation_date = forms.DateField(
        label='Date of installation')
    last_pump_date = forms.DateField(label='Date of last pump')
    last_instpection_date = forms.DateField(
        label='Date of last inspection')
    inspection_document = forms.FileField(label='Proof of inspection')
