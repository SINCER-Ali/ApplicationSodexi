from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def utilities(request):
    return render(request, 'utilities.html')