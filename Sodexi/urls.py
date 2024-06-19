from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('appSodexi.urls')),
]
