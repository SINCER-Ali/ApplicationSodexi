from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User


class CustomPasswordResetForm(SetPasswordForm):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Aucun utilisateur n'est associé à cet email.")
        return email



