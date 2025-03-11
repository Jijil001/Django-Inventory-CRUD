from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html', {})

# Show all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})

# Add a new product
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Product'})

# Update an existing product
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'form.html', {'form': form, 'title': 'Update Product'})

    
# Delete a product
def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('product-list')