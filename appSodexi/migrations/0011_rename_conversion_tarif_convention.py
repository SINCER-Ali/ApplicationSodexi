# Generated by Django 5.0.6 on 2024-06-17 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSodexi', '0010_iatacsvfile_rename_lata_iata_delete_latacsvfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarif',
            old_name='conversion',
            new_name='convention',
        ),
    ]