from django.contrib import admin
from django.urls import path
from journal.views import AddEntry



urlpatterns = [
    path("journal/add-entry/", AddEntry.as_view(), name="add_entry"),

]