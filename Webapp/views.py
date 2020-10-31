from django.shortcuts import render
from django.http import HttpResponseRedirect
from Webapp.models import Products,AddtoCard
import base64
# Create your views here.
def Home_Page(request):
    return render(request,"MyApp/home.html")

def Shop_Page(request):
    return render(request,"MyApp/shop.html")

def ShopKeeper(request):
    return render(request,"MyApp/shopkeeper.html")

def ProductSaved(request):
    Shopname = request.POST.get('shop_name')
    products = Products.objects.filter(Shopname=Shopname)
    if products.count()>0:
        return render(request,"MyApp/products.html",{'products':products,'shop':Shopname})
    else:
        return render(request, "MyApp/products.html", {'message': 'No Products'})

def Add_to_Cart(request):
    cart = request.POST.get('product_id')
    Get_Cart = AddtoCard.objects.filter(productid=cart)
    shop = Products.objects.filter(id=cart)
    if Get_Cart.count()>0:
        for shops in shop:
            Shopname=shops.Shopname
            products = Products.objects.filter(Shopname=Shopname)
            return render(request,"MyApp/products.html",{"message":"Product is Already added to the Cart",'products':products,'shop':Shopname})
    else:
        for shops in shop:
            Shopname = shops.Shopname
            products = Products.objects.filter(Shopname=Shopname)
            AddtoCard(productid=cart).save()
            return render(request,"MyApp/products.html",{"message":"Product is added to Cart",'products':products,'shop':Shopname})

def Show_Product(request):
    show = AddtoCard.objects.all()
    for product in show:
        id = product.productid
        pro = Products.objects.filter(id=id)
        return render(request,"MyApp/showproduct.html",{"pro":pro})