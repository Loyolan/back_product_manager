from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Produit
from app.serializers import ProduitSerializer
from django.core.exceptions import ValidationError

# Create your views here.
@api_view(['GET'])
def allProduits(r):
	try:
		produits = Produit.objects.all()
		produitsSerializers = ProduitSerializer(produits, many=True)
		prix_minimal = 0
		prix_maximal = 0
		total = 0
		for produit in produits:
			if prix_minimal > produit.prix or prix_minimal == 0:
				prix_minimal = produit.prix
			if prix_maximal < produit.prix:
				prix_maximal = produit.prix
			total += produit.prix * produit.quantite
		res = {'produits': produitsSerializers.data, 'prix_minimal': prix_minimal, 'prix_maximal': prix_maximal, 'total': total}
	except:
		res = {'status': 'warning', 'message': 'Une eurreur se produite lors de la recuperation de donnees'}
	return Response(res)

@api_view(['GET'])
def getProduitByNum(r, num):
	try:
		produit = Produit.objects.get(numProduit=num)
		produitSerializer = ProduitSerializer(produit, many=False)
		res = produitSerializer.data
	except ValidationError:
		res = {'status': 'error', 'message': 'Identifiant Invalide'}
	except:
		res = {'status': 'warning', 'message': 'Donnee introuvable'}
	return Response(res)

@api_view(['POST'])
def addProduit(r):
	try:
		serialisation = ProduitSerializer(data=r.data, many=False)
		res = None
		if serialisation.is_valid():
			serialisation.save()
			res = {'status': 'success', 'data': serialisation.data, 'message': 'Creation d\'un produit reussi!'}
		else:
			res = {'status': 'error', 'message': 'Entrees invalide'}
	except:
		res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
	return Response(res)

@api_view(['PUT'])
def updateProduit(r, num):
	try:
		produit = Produit.objects.get(numProduit=num)
		produit.design = r.data['design']
		produit.prix = r.data['prix']
		produit.quantite = r.data['quantite']
		produit.save()
		res = {'status': 'success', "message": "Mis à jour des infos réussi"}
	except ValidationError:
		res = {'status': 'error', 'message': "Produit introuvable"}
	except:
		res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
	return Response(res)

@api_view(['DELETE'])
def deleteProduit(r, num):
	try:
		produit = Produit.objects.get(numProduit=num)
		produit.delete()
		res = res = {'status': 'success', 'message': 'Suppression d\'un produit réussi'}
	except ValidationError:
		res = {'status': 'error', 'message': 'produit introuvable'}
	except:
		res = {'status': 'error', 'message': 'Erreur, Veuillez essayer plus tard'}
	return Response(res)