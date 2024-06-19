from django.db import models


class Iata(models.Model):
    iata_pays = models.CharField(max_length=2)
    iata_escale = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.iata_pays} -> {self.iata_escale}"


class IataCSVFile(models.Model):
    file = models.FileField(upload_to='csv_filesiata/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
