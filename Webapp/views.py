from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from Webapp.models import Products,AddtoCard,register
import base64
# Create your views here.
def Home_Page(request):
    return render(request,"MyApp/home.html")

def Login(request):
    if request.POST:
        useremail= request.POST.get('email')
        password = request.POST.get('password')
        count = register.objects.filter(email=useremail,password=password)
        if count.count()>0:
            request.session['useremail'] = useremail

            return redirect("/", {'useremail':useremail})
        else:
            return render(request,"MyApp/login.html",{'message':'Invalid User or Password'})


def Logout(request):
      request.session.flush()
      return redirect("/")

def Registration_Page(request):
    return render(request,"MyApp/registration.html")


def SaveRegister(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    auth=register.objects.filter(email=email).count()
    if auth>0:
        message="User Already Registered With This User"
        return render(request, "MyApp/registration.html", {'message': message})
    else:
        register(username=username, email=email, password=password).save()
    return render(request, "MyApp/login.html")


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
        return render(request,"MyApp/showproduct.html",{"pro":pro,"show":show})