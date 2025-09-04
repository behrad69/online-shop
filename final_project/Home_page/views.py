from django.shortcuts import render
from django.apps import apps
from django.shortcuts import get_object_or_404
# Create your views here.
def base_web(request):
    products = apps.get_model('commodity', 'product').objects.all()
    return render(request, 'index.html',{'products': products})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')