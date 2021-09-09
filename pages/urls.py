from django.urls import path
from . import views

urlpatterns = [
    path('productcxvzfbxfhxdfbxc', views.product, name="product_list"),
    path('category', views.category),
]
