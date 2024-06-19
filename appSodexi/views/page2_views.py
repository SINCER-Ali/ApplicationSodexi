from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def page2(request):
    return render(request, 'page2.html')