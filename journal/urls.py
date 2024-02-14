from django.contrib import admin
from django.urls import path
from. import views



urlpatterns = [
    path("journal/add-entry/", views.add_entry, name='add-entry')

]