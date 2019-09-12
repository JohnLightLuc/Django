from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def produit(request):
    return render(request, 'pages/produit.html')

def checkout(request):
    return render(request, 'pages/checkout.html')
