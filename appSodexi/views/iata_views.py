from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms.iataCSVUploadForm import IataCSVUploadForm
from ..models import Iata
import csv

@login_required
def iata_upload_form(request):
    if request.method == 'POST':
        form = IataCSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')
            for row in reader:
                iata_pays = row['Iata Pays']
                iata_escale = row['Iata Escale']
                Iata.objects.create(
                    iata_pays=iata_pays,
                    iata_escale=iata_escale
                )
            messages.success(request, "Le fichier CSV pour Iata a été importé avec succès.")
            return redirect('admin:appSodexi_iata_changelist')
    else:
        form = IataCSVUploadForm()

    return render(request,dict(form=form))