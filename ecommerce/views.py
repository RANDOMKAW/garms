from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from ecommerce.models import  *

def home(request):
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    marque=Marque.objects.get(nomMarque="Supreme")
    brandArticles=Article.objects.filter(marque=marque)

    return render(request, 'ecommerce/base.html', {'brandArticles': brandArticles, 'articles': articles})





def collections(request):
    """
    Vue qui affiche les différentes collections.
    """
    return HttpResponse(
        """
        <h1>Collections</h1>
        <p>Cette page contiendra les futures collections de Garms</p>
        """
    )
def tousProduits(request):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.all()
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
    marque=Marque.objects.get(nomMarque=id_marque)
    articles=Article.marque.filter(marque=marque)
    return render(request, "ecommerce/listing.html", {'articles':articles})


def article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    article=Article.objects.get(slug=id_article)
    return render(request, "ecommerce/produit.html", {'article':article})
