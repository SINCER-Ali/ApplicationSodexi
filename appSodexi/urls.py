from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views.calculatrice_views import calculateur_tarif
from .views.home_view import home
from .views.iata_views import iata_upload_form
from .views.page2_views import page2
from .views.pages_views import pages
from .views.profil_views import profil
from .views.tarif_views import tarif_upload_form
from .views.utilities_views import utilities

urlpatterns = [
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=
         reverse_lazy('appSodexi:password_reset_complete')), name="password_reset_confirm"),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='done', html_email_template_name=
         'registration/password_reset_email.html'), name='password_change'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home, name='home'),
    path('pages/', pages, name='pages'),
    path('utilities/', utilities, name='utilities'),
    path('page2/', page2, name='page2'),
    path('profil/', profil, name='profil'),

    path('admin-csv/appSodexi/iata/import-csv/', iata_upload_form, name='iata_upload_form'),
    path('admin-csv/appSodexi/tarif/import-csv/', tarif_upload_form, name='tarif_upload_form'),

    path('calculateur-tarif/', calculateur_tarif, name='calculateur_tarif'),
]
