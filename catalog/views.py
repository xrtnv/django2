import pathlib

from django.shortcuts import render


# Create your views here.
def main_page(req):
    return render(req, "catalog/templates/catalog/home.html")

def contacts_view(req):
    return render(req, "catalog/templates/catalog/contacts.html")