from django.shortcuts import render
from django.http import HttpResponse
from ..models.cydtraitement_models import Cyd
from ..utils import parse_file, generate_pdf
import io
from django.conf import settings
import os

def upload_file_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        parse_file(file_path)
        return HttpResponse("Fichier analysé et données enregistrées avec succès")
    return render(request, 'import_cyd40.html')

def generate_pdf_view(request):
    cyd_objects = Cyd.objects.all()
    buffer = io.BytesIO()
    generate_pdf(cyd_objects, buffer)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="rapport_vente.pdf"'
    return response
