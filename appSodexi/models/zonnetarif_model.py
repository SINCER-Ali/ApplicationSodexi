from django.db import models


class Tarif(models.Model):
    origine = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    minimum = models.IntegerField()
    convention = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.origine} -> {self.destination}"


class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
