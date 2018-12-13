from django.db import models
from django.utils import timezone

class Article(models.Model):
    nomProduit = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True)
    description = models.TextField(null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    categorie=models.CharField(max_length=42, null=True)
    image=models.ImageField(upload_to="photos/",default='../../../../../static/img/GarmsSmallLogo.jpg')
    genre=models.CharField(max_length=42, null=True)
    date=models.DateTimeField(default=timezone.now, verbose_name="Date d'upload")




    class Meta:
        verbose_name = "article"
        ordering = ['date']


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomProduit

class Marque(models.Model):
    nomMarque = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True)
    description = models.TextField(null=True)
    image=models.ImageField(upload_to="photos/",default='../../../../../static/img/GarmsSmallLogo.jpg')
    produits = models.ManyToManyField(Article, related_name="marques")
    class Meta:
        verbose_name = "marque"
        ordering = ['nomMarque']


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomMarque

class Collection(models.Model):
    nomCollection = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True)
    description = models.TextField(null=True)
    image=models.ImageField(upload_to="photos/",default='../../../../../static/img/GarmsSmallLogo.jpg')
    produits = models.ManyToManyField(Article, related_name="collections")
    class Meta:
        verbose_name = "collection"
        ordering = ['nomCollection']


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nomCollection
