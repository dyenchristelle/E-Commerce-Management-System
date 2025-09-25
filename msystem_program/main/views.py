from django.shortcuts import render

# Create your views here.
def user_index(request):
    return render(request, "main/user/user-index.html")

def admin_index(request):
    return render(request, "main/admin/admin-index.html")

def admin_homepage(request):
    return render(request, "main/admin/homepage.html")