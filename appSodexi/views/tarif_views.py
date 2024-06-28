from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms.csv_uploadform import CSVUploadForm
from ..models import Tarif
import csv

@login_required
def tarif_upload_form(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')
            for row in reader:
                origine = row['Orig']
                destination = row['Dest']
                try:
                    minimum = int(row['MIN'])
                    convention = float(row['CONV'].replace(',', '.'))
                except ValueError as e:

                    messages.warning(request, f"Il y a eu une erreur lors de la conversion des données: {str(e)}")
                    continue

                Tarif.objects.update_or_create(
                    origine=origine,
                    destination=destination,
                    defaults={'minimum': minimum, 'convention': convention}
                )

            messages.success(request, "Le fichier CSV pour Tarif a été importé avec succès.")
            return redirect('admin:appSodexi_tarif_changelist')
    else:
        form = CSVUploadForm()

    return render(request,dict(form=form))
