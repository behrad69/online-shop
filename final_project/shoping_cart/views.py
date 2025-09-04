from django.shortcuts import render,redirect
from django.apps import apps
from django.shortcuts import get_object_or_404
from .forms import cartform
from django.http import HttpResponse
# Create your views here.
def cart_view(request, id):
    products = apps.get_model('commodity', 'product').objects.all()
    requested_product = apps.get_model('commodity', 'product').objects.all()
    requested_product = get_object_or_404(requested_product, id=id)
    if request.user.is_authenticated:
        return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})
    else:
        return redirect('login')
    
def select_product(request, id):
    products = apps.get_model('commodity', 'product').objects.all()
    requested_product = apps.get_model('commodity', 'product').objects.all()
    requested_product = get_object_or_404(requested_product, id=id)
    
    if request.method == 'POST':
        form = cartform(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.price = requested_product.price  # From database
            cart_item.product_name = requested_product.name  # From database  
            cart_item.user = request.user  # From logged in user
            form.save()
            return redirect('goods')
    else:
        form = cartform()
        return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})
    return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})