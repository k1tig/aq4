from django.contrib import admin
from django.urls import path, include
from catalog.views import AddScapeView, AddPlantView, HomePageView, UpdateScapeView, UpdatePlantView, ScapeView, ScapeListView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("catalog/add-scape/", AddScapeView.as_view(), name="add_scape"),
    path("catalog/scape/", ScapeListView.as_view(), name="list_scape"),
    path("catalog/update-scape/<int:pk>", UpdateScapeView.as_view(), name="update_scape"),
    path("catalog/scape/<int:pk>", ScapeView.as_view(), name="scape_view"),
    path("catalog/add-plant/", AddPlantView.as_view(), name="add_plant"),
    path("catalog/update-plant/<int:pk>", UpdatePlantView.as_view(), name="update_plant")

]