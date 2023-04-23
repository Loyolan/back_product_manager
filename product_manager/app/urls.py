from django.urls import path
from app import views

urlpatterns = [
	path('', views.allProduits),
	path('add', views.addProduit),
	path('<num>/', views.getProduitByNum),
	path('<num>/update', views.updateProduit),
	path('<num>/delete', views.deleteProduit)
]