from django.db import models

class Wohnort(models.Model):
    name = models.CharField(max_length = 100)
    
class PLZ(models.Model):
    zahl = models.CharField(max_length = 5)

class Position(models.Model):
    bezeichnung = models.CharField(max_length = 50)

class Mitarbeiter(models.Model):
    name = models.CharField(max_length = 50)
    vorname = models.CharField(max_length = 50)
    position = models.ManyToManyField(Position, through = 'MitarbeiterPosition')

    geburtsdatum = models.DateField()
    anlegedatum = models.DateTimeField(auto_now_add = True)

    strasse = models.CharField(max_length = 50)
    hausnummer = models.CharField(max_length = 5)
    wohnort = models.ForeignKey(Wohnort)
    plz = models.ForeignKey(PLZ)

class MitarbeiterPosition(models.Model):
    mitarbeiter = models.ForeignKey(Mitarbeiter)
    position = models.ForeignKey(Position)
    von = models.DateField()
    bis = models.DateField()
    aktiv = models.BooleanField(default = False)