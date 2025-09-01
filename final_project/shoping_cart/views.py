from django.shortcuts import render
from django.apps import apps
from django.shortcuts import get_object_or_404
# Create your views here.
def cart_view(request, id):
    products = apps.get_model('commodity', 'product').objects.all()
    requested_product = apps.get_model('commodity', 'product').objects.all()
    requested_product = get_object_or_404(requested_product, id=id)
    return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})