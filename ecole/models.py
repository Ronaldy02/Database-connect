from django.db import models

# Create your models here.
from django.db import models


class Etudiants(models.Model):
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='Pays', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.IntegerField(db_column='Telephone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etudiants'
