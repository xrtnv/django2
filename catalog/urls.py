from django.urls import path

from catalog.views import main_page, contacts_view

urlpatterns = [
    path('', main_page),
    path('contacts/', contacts_view)
]