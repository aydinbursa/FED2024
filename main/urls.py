from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("index.html", views.main),
    path("clients.html", views.clients),
    path("facture.html", views.factures),
    path("devis.html", views.devis),
    path("documents.html", views.documents),
    path("articles.html", views.articles),
    path("settings.html", views.settings),
    path("login.html", views.login),
    path("404.html", views.p404),
]