"""NOGOZO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView, ListView
from django.contrib import admin
from django.urls import path
from Webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home_Page),
    path('logout/',views.Logout),
    path('applicant/', TemplateView.as_view(template_name="MyApp/login.html")),
    path('applog/',views.Login),
    path('register/',views.Registration_Page),
    path('savedetail/',views.SaveRegister),
    path('home/',views.Home_Page),
    path('shop/',views.Shop_Page),
    path('keeper/',views.ShopKeeper),
    path('product/',views.ProductSaved),
    path('add_to_cart/',views.Add_to_Cart, name='addtocart'),
    path('showproduct/',views.Show_Product),

]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)