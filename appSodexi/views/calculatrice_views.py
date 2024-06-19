from django.shortcuts import render
from ..forms.calculatrice import TarifForm
from ..models import Tarif


def calculateur_tarif(request):
    form = TarifForm()
    tarif_info = None
    if request.method == 'POST':
        form = TarifForm(request.POST)
        if form.is_valid():
            origine = form.cleaned_data['origine']
            destination = form.cleaned_data['destination']
            try:
                tarif_info = Tarif.objects.get(origine=origine, destination=destination)
            except Tarif.DoesNotExist:
                tarif_info = None

    return render(request, 'calculateur_tarif.html', {'form': form, 'tarif_info': tarif_info})
