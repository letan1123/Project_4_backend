from django.urls import path
from . import views

urlpatterns = [
    path('api/species', views.SpeciesList.as_view(), name='species_list'),
    path('api/species/<int:pk>', views.SpeciesDetail.as_view(), name='species_detail'),
]
