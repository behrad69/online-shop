from django.shortcuts import render,redirect
from django.apps import apps
from django.shortcuts import get_object_or_404
from .forms import cartform
from django.http import HttpResponse
from .models import cart
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
            cart_item.img = requested_product.image  # From database  
            cart_item.user = request.user  # From logged in user
            form.save()
            return redirect('goods')
    else:
        form = cartform()
        return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})
    return render(request, 'shop-single.html', {'products': products, 'requested_product': requested_product})

def bills(request):
    count = cart.objects.filter(user=request.user).count()
    order = cart.objects.all()
    user = request.user
    sum = 0
    for i in order:
        if (i.user == user):
            sum += i.price * i.quantity
    total = sum + 10000
    return render(request,'checkout.html',{'order' : order, 'count': count, 'user': user,'sum': sum,'total': total})
def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(cart, id=item_id, user=request.user)
        item.delete()
        return redirect('paywall')