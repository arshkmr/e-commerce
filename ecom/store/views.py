from django.shortcuts import render
from . models import Product

# Create your views here.
def home(reqeust):
    products = Product.objects.all()
    return render(reqeust, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})
