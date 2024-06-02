from django.http import HttpResponse
from django.shortcuts import redirect, render

def main(request):
    return render(request, 'index.html')

def clients(request):
    return render(request, "clients.html")

def factures(request):
    return render(request, "facture.html")

def devis(request):
    return render(request, "devis.html")

def documents(request):
    return render(request, "documents.html")

def articles(request):
    return render(request, "articles.html")

def settings(request):
    return render(request, "settings.html")

def login(request):
    return render(request, "login.html")

def p404(request):
    return render(request, "404.html")

def n_facture(request):
    return render(request, "n_facture.html")

def n_client(request):
    return render(request, "n_client.html")

def n_devis(request):
    return render(request, "n_devis.html")