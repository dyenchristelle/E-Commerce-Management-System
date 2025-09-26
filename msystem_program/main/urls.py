from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),   # homepage
    path("admin-home/", views.admin_index, name="admin_index"),
    path('admin-homepage/', views.admin_homepage, name="admin-homepage"),
    path('admin-products', views.admin_products, name="admin-products"),
    path('add-product/', views.add_product, name='add_product'),
]