from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from ecommerce.models import  *

def home(request):
    articles = Article.objects.all().order_by("date") # Nous sélectionnons tous nos articles

    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    marque1=marques.order_by("?").first()
    marque2=marques.order_by("?").first()
    while marque1==marque2:
            marque2=marques.order_by("?").first()

    brandArticles1=marque1.produits.all().order_by("?")
    brandArticles2=marque2.produits.all().order_by("?")

    promoslides=PromoSlideshow.objects.order_by("date")


    return render(request, 'ecommerce/base.html', {'marques':marques, 'collections':collections, 'brandArticles1': brandArticles1,'brandArticles2': brandArticles2, 'articles': articles, 'marque1':marque1, 'marque2':marque2, 'promoslides': promoslides})


def collections(request):
    """
    Vue qui affiche les différentes collections.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    return render(request, "ecommerce/listing_collections.html", {'marques':marques, 'collections':collections})

def marques(request):
    """
    Vue qui affiche les différentes marques.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    return render(request, "ecommerce/listing_marques.html", {'marques':marques, 'collections':collections})


def tousProduits(request):
    """
    Vue qui affiche la collection sélectionnée.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    if 'p' in request.GET:
        page = request.GET['p']
    else:
        page=1
    nbmin=(page-1)*3
    nbmax=page*3
    articles=Article.objects.all().filter(id__gte=nbmin).filter(id__lte=nbmax)
    nbPages=0
    print(articles)
    return render(request, "ecommerce/listing.html", {'articles':articles, 'marques':marques, 'collections':collections, 'page': page, 'nbPages': nbPages})

def new_listing(request):
    """
    Vue qui affiche la collection sélectionnée.
    """
    articles=Article.objects.all().order_by("date")
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    nbArticlesParPage=3
    if len(articles) % nbArticlesParPage == 0:
        nbPages=len(articles)//nbArticlesParPage
    else:
        nbPages=len(articles)//nbArticlesParPage +1
    str=""
    for i in range(0,nbPages):
        str+="x"
    if 'p' in request.GET:
        page = request.GET['p']
    else:
        page=1

    nbmin=(int(page)-1)*3
    nbmax=int(page)*3
    articles=Article.objects.all().filter(id__gte=nbmin).filter(id__lte=nbmax)



    return render(request, "ecommerce/listing.html", {'articles':articles, 'marques':marques, 'collections':collections, 'page': page, 'str': str})


def collection_listing(request, id_collection):
    """
    Vue qui affiche la collection sélectionnée.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    articles=Collection.objects.get(slug=id_collection).produits.all()
    if 'q' in request.GET:
        page = request.GET['p']
    else:
        page=1

    return render(request, "ecommerce/listing.html", {'articles':articles, 'marques':marques, 'collections':collections, 'page': page})
def marque_listing(request, id_marque):
    """
    Vue qui affiche la collection sélectionnée.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    articles=Marque.objects.get(slug=id_marque).produits.all()

    if 'q' in request.GET:
        page = request.GET['p']
    else:
        page=1

    return render(request, "ecommerce/listing.html", {'articles':articles, 'marques':marques, 'collections':collections, 'page': page})
def genre_listing(request, gender):
    """
    Vue qui affiche la collection sélectionnée.
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    articles=Article.objects.filter(genre=gender)

    if 'q' in request.GET:
        page = request.GET['p']
    else:
        page=1

    return render(request, "ecommerce/listing.html", {'articles':articles, 'marques':marques, 'collections':collections, 'page': page})

def article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --
    article=Article.objects.get(slug=id_article)
    return render(request, "ecommerce/produit.html", {'article':article, 'marques':marques, 'collections':collections})


def cart(request):
    """
    Vue qui affiche le panier et les produits de l'utilisateur
    """
    #Importé pour les besoins du menu
    marques=Marque.objects.all().order_by("nomMarque")
    collections=Collection.objects.all().order_by("nomCollection")
    # --

    articles=Article.objects.all()

    return render(request, "ecommerce/cart.html", {'articles':articles, 'marques':marques, 'collections':collections})

def static(request,static_page):
    page=Page.objects.get(slug=static_page)
    return render(request, "ecommerce/static.html", {'page': page })
