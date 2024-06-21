from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def import_cyd40(request):
    return render(request, 'import_cyd40.html')