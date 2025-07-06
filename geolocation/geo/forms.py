from django import forms

class GeoForm(forms.Form):
    initial = forms.CharField(label='Initial location', max_length=100, required=True)
    destination = forms.CharField(label='Destination', max_length=100, required=True)