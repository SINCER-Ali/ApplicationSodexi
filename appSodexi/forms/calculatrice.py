from django import forms
from ..models import Tarif

class TarifCalculatorForm(forms.Form):
    origine = forms.ChoiceField(choices=[])
    destination = forms.ChoiceField(choices=[]) 
    poids_kg = forms.IntegerField(label='Poids en kg')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mettre à jour les choix pour origine
        origines = Tarif.objects.values_list('origine', flat=True).distinct().order_by('origine')
        self.fields['origine'].choices = [(origine, origine) for origine in origines]

        # Mettre à jour les choix pour destination
        destinations = Tarif.objects.values_list('destination', flat=True).distinct().order_by('destination')
        self.fields['destination'].choices = [(destination, destination) for destination in destinations]

    def clean(self):
        cleaned_data = super().clean()
        origine = cleaned_data.get('origine')
        destination = cleaned_data.get('destination')
        poids_kg = cleaned_data.get('poids_kg')

        if origine and destination and poids_kg is not None:
            try:
                tarif_info = Tarif.objects.get(origine=origine, destination=destination)
                if poids_kg < tarif_info.minimum:
                    self.add_error('poids_kg', f"Le poids minimum requis est {tarif_info.minimum} kg")
                else:
                    cout_estime = poids_kg * tarif_info.convention
                    cleaned_data['cout_estime'] = cout_estime
            except Tarif.DoesNotExist:
                self.add_error('origine', "Aucun tarif trouvé pour ce routing")

        return cleaned_data
