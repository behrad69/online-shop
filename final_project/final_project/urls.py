"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shoping_cart.views import cart_view,select_product,bills,delete_item
from Home_page.views import about,contact,base_web
from commodity.views import goods
from authentication.views import register,login_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_web, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cart/<int:id>/', cart_view, name='cart'),
    path('cart/<int:id>/checkout/', select_product, name='checkout'),
    path('bills/', bills, name='paywall'),
    path('bills/<int:item_id>/delete/', delete_item, name='deletion'),
    path('commodity/', goods, name='goods'),
    path('id/', register, name='identification'),
    path('signin/', login_user, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
