# Generated by Django 5.0.6 on 2024-06-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSodexi', '0005_tarif_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_pays', models.CharField(max_length=2)),
                ('iata_escale', models.CharField(max_length=3)),
            ],
        ),
    ]