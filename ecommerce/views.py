from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from ecommerce.models import  *

def home(request):
    articles = Article.objects.all().order_by("date") # Nous sélectionnons tous nos articles
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collections.objects.all().order_by("nomMarque")
    marque1=marques.order_by("?").first()
    marque2=marques.order_by("?").first()
    while marque1==marque2:
            marque2=marques.order_by("?").first()

    brandArticles1=marque1.produits.all().order_by("?")
    brandArticles2=marque2.produits.all().order_by("?")


    return render(request, 'ecommerce/base.html', {'marques':marques, 'collections':collections, 'brandArticles1': brandArticles1,'brandArticles2': brandArticles2, 'articles': articles, 'marque1':marque1, 'marque2':marque2})


def collections(request):
    """
    Vue qui affiche les différentes collections.
    """
    collections=Collection.objects.all()
    return render(request, "ecommerce/listing_collections.html", {'collections':collections})

def marques(request):
    """
    Vue qui affiche les différentes marques.
    """
    marques=Marque.objects.all()
    return render(request, "ecommerce/listing_marques.html", {'marques':marques})


def tousProduits(request):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.all()
    return render(request, "ecommerce/listing.html", {'articles':articles})

def new_listing(request):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.all().order_by("date")
    return render(request, "ecommerce/listing.html", {'articles':articles})

def collection_listing(request, id_collection):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.filter(collection=id_collection)
    return render(request, "ecommerce/listing.html", {'articles':articles})

def marque_listing(request, id_marque):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Marque.objects.get(slug=id_marque).produits.all()

    return render(request, "ecommerce/listing.html", {'articles':articles})

def genre_listing(request, gender):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.filter(genre=gender)

    return render(request, "ecommerce/listing.html", {'articles':articles})


def article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    article=Article.objects.get(slug=id_article)
    return render(request, "ecommerce/produit.html", {'article':article})
