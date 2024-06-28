from django import forms


class UploadFileForm(forms.Form):
    document = forms.FileField(label='Fichier TXT pour CYD40')
