from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def visualiser_cyd40(request):
    return render(request, 'visualiser_cyd40.html')