from django import forms


class IataCSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Fichier CSV pour Iata')
