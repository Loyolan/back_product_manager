from django.db import models

# Create your models here.
class Produit(models.Model):
	numProduit = models.AutoField(primary_key=True)
	design = models.CharField(max_length=255)
	prix = models.IntegerField()
	quantite = models.IntegerField()
