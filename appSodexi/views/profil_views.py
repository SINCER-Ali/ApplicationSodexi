from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profil(request):
    return render(request, 'profil.html')