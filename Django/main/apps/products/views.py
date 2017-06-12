from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.

# Load product page
def index(request):
    brand = Brand.object.all();
    product = Product.object.all();
    context = {
        "brand": "brands",
        "producs": "products",
    }

    return render(request, 'products/index.html', context)

# Add new product(s)
def add(request):
    brand = Brand.objects.get(brand_name = request.POST['brand_name'])
    Product.objects.create(brand=brand, name=request.POST['name']. ['price'], date_added=datetime.now(), description=request.POST['description'])

    return redirect('/products')

# Delete product(s)
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/products')

# Edit/product info
def edit(request, id):
    context = [
        "product": Product.objects.get(id=id),
        "brand": Brand.objects.all(),
    ]
    return render(request, 'inventory/edit.html', context)

# Update product  info
def update(request, id):
    brand = Brand.objects.get(brand_name=request.POST['brand_name'])
    product = Product.objects.get(id=id)
    product.brand = brand
    product.name = request.POST['name']
    product.price = request.POST['price']
    product.description = request.POST['descritpion']
    product.save()

    returm redirect('/products')
