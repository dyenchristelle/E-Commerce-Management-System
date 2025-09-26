from django.shortcuts import render, redirect
from .models import AdminLogin
from .models import Products

# Create your views here.
def user_index(request):
    return render(request, "main/user/user-index.html")

def admin_index(request):
    return render(request, "main/admin/admin-index.html")

def admin_homepage(request):
    return render(request, "main/admin/homepage.html")

def admin_products(request):
    return render(request, "main/admin/products.html")



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            if AdminLogin.objects.filter(username=username, password=password).exists():
                return redirect("admin-homepage")
        except AdminLogin.DoesNotExist:
            return render(request, "main/admin/admin-index.html", {"error": "Invalid username or password"})
        
    return render(request, "main/admin/admin-index.html")


def admin_homepage(request):
    return render(request, "main/admin/homepage.html")

def products(request):
    products = Products.objects.all()
    return render(request, "main/admin/products.html", {"products": products})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("Product_Name")
        quantity = request.POST.get("Quantity")
        price = request.POST.get("Price")
        Products.objects.create(name=name, quantity=quantity, price=price)
        print("Item added.")
        return redirect("products")
        
    