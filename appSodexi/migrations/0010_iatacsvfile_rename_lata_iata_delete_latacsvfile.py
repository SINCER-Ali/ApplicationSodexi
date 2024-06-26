# Generated by Django 5.0.6 on 2024-06-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSodexi', '0009_lata_created_at_lata_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='IataCSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_filesiata/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Lata',
            new_name='Iata',
        ),
        migrations.DeleteModel(
            name='lataCSVFile',
        ),
    ]
