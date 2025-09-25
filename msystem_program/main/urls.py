from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),   # homepage
    path("admin-home/", views.admin_index, name="admin_index"),
]