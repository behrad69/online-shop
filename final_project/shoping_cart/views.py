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
        # User is logged in
        if request.method == 'POST':
        # Collect all the data they entered
            form = cartform(request.POST)
        
        # Check if the data is valid (correct email format, etc.)
            if form.is_valid():
            # Save the data to database
                form.save()
            # Redirect to a success page
        return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})
    else:
        # User is not logged in
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
            return HttpResponse('fuck')
    else:
        form = cartform()
        return HttpResponse('shit')
    return HttpResponse('wtf')