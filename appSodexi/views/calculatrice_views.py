from django.shortcuts import render
from ..forms.calculatrice import TarifCalculatorForm
from ..models import Tarif

def calculateur_tarif(request):
    form = TarifCalculatorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        tarif_infos = Tarif.objects.filter(origine=form.cleaned_data['origine'], destination=form.cleaned_data['destination'])
        if tarif_infos.exists():
            tarif_info = tarif_infos.first()
            cout_estime = form.cleaned_data['poids_kg'] * tarif_info.convention
            return render(request, 'calculatrice.html', {
                'form': form,
                'tarif_info': tarif_info,
                'cout_estime': cout_estime,
            })
        else:
            form.add_error(None, "Aucun tarif trouvé pour cette origine et destination.")
            return render(request, 'calculatrice.html', {'form': form})

    return render(request, 'calculatrice.html', {'form': form})