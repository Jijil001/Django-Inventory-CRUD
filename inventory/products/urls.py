from django.urls import path
from .views import product_list, add_product, update_product, delete_product

urlpatterns = [
    path('', product_list, name='product-list'),
    path('add/', add_product, name='add-product'),
    path('update/<int:pk>/', update_product, name='update-product'),
    path('delete/<int:pk>/', delete_product, name='delete-product'),
]
