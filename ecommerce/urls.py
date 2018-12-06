from django.urls import path
from . import views

urlpatterns = [
        path('collections',views.collections),
        path('collections/all', views.tousProduits),
        path('collections/<id_collection>', views.collection_listing),
        path('brands/<id_marque>', views.marque_listing),
        path('article/<id_article>', views.article),
]
