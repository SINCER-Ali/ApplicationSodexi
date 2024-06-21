from django.shortcuts import render
from ..forms.calculatrice import TarifCalculatorForm
from ..models import Tarif

def calculateur_tarif(request):
    form = TarifCalculatorForm(request.POST or None)
    cout_estime = None
    cout_cession = None
    tarif_info = None  # Ajout d'une variable tarif_info pour stocker les détails du tarif

    if request.method == 'POST' and form.is_valid():
        if 'calculate_convention' in request.POST:
            origine = form.cleaned_data['origine']
            destination = form.cleaned_data['destination']
            poids_kg = form.cleaned_data['poids_kg']

            try:
                tarif_info = Tarif.objects.get(origine=origine, destination=destination)
                if poids_kg < tarif_info.minimum:
                    form.add_error('poids_kg', f"Le poids minimum requis est {tarif_info.minimum} kg")
                else:
                    cout_estime = poids_kg * tarif_info.convention
            except Tarif.DoesNotExist:
                form.add_error(None, "Aucun tarif trouvé pour cette origine et destination.")
        elif 'calculate_cession' in request.POST:
            cout_cession = form.calculate_cout_cession()

    return render(request, 'calculatrice.html', {
        'form': form,
        'cout_estime': cout_estime,
        'cout_cession': cout_cession,
        'tarif_info': tarif_info,  # Passer tarif_info au template
    })
