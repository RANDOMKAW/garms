from django.urls import path
from . import views

urlpatterns = [
        path('collections',views.collections, name="collections"),
        path('marques',views.marques, name="marques"),
        path('new', views.new_listing, name="new_listing"),
        path('collection/<id_collection>', views.collection_listing, name="collection_listing"),
        path('brands/<id_marque>', views.marque_listing, name="marque_listing"),
        path('genre/<gender>', views.genre_listing, name="genre_listing"),
        path('article/<id_article>', views.article, name="article"),

]
