
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origine', models.CharField(max_length=2)),
                ('destination', models.CharField(max_length=2)),
                ('temps_minimum', models.IntegerField()),
                ('conversion', models.FloatField()),
            ],
        ),
    ]
