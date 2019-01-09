from django.contrib import admin
from .models import  *
from django.utils.text import Truncator

class ArticleAdmin(admin.ModelAdmin):
    fields = ('nomProduit', 'slug', 'description','genre','prix','categorie','image')
    list_display   = ('nomProduit','apercu_description','genre','prix','categorie','date')
    list_filter    = ('categorie', 'genre')
    date_hierarchy = 'date'
    ordering       = ('date', )
    #search_fields  = ('titre', 'contenu')
    def apercu_description(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.

        On pourrait le coder nous même, mais Django fournit déjà la
        fonction qui le fait pour nous !
        """
        return Truncator(article.description).chars(40, truncate='...')
    apercu_description.short_description = 'Description'

admin.site.register(Article,ArticleAdmin)


class MarqueAdmin(admin.ModelAdmin):
    fields = ('nomMarque', 'slug', 'apercu_description','produits','image')
    list_display   = ('nomMarque', 'slug', 'apercu_description')
    filter    = ('nomMarque')
    ordering       = ('nomMarque', )

    def apercu_description(self, marque):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.

        On pourrait le coder nous même, mais Django fournit déjà la
        fonction qui le fait pour nous !
        """
        return Truncator(marque.description).chars(40, truncate='...')
    apercu_description.short_description = 'Description'


admin.site.register(Marque,MarqueAdmin)


class CollectionAdmin(admin.ModelAdmin):
    fields = ('nomCollection', 'slug', 'description','produits','image')
    list_display   = ('nomCollection', 'slug', 'description')
    filter    = ('nomCollection')
    ordering       = ('nomCollection', )

    def apercu_description(self, collection):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.

        On pourrait le coder nous même, mais Django fournit déjà la
        fonction qui le fait pour nous !
        """
        return Truncator(collection.description).chars(40, truncate='...')
    apercu_description.short_description = 'Description'


admin.site.register(Collection,CollectionAdmin)

class PromoSlideshowAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'image','date' )
    list_display   = ('title', 'content','image', 'date',)
    filter    = ('title')
    ordering       = ('title', )




admin.site.register(PromoSlideshow,PromoSlideshowAdmin)


class PageAdmin(admin.ModelAdmin):
    fields = ('nomPage','slug', 'content', )
    list_display   = ('nomPage', 'content')
    filter    = ('nomPage')
    ordering       = ('nomPage', )



admin.site.register(Page, PageAdmin)
