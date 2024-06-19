from django import forms

class TarifForm(forms.Form):
    origine = forms.CharField(label='Origine', max_length=255)
    destination = forms.CharField(label='Destination', max_length=255)
