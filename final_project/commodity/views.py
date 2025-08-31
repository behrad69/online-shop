from django.shortcuts import render
from .models import product
# Create your views here.
def goods(request):
    products = product.objects.all()
    return render(request, 'shop.html', {'products': products})
