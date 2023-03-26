from django.shortcuts import render

from .models import Category, Product

from django.shortcuts import get_object_or_404

def home_page (request) :

    all_products = Product.objects.all()

    ctx = {
        'products' : all_products,
    }
    return render(request, 'store/home_page.html', ctx)


def categories(request) :
    all_categories = Category.objects.all()
    return {'all_categories' : all_categories}

def product_info (request, product_slug):
     single_product = get_object_or_404(Product, slug = product_slug)
     ctx = {
         "product" : single_product,
     }
     return render (request,'store/product-info.html',ctx)

def list_category (request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)

    products = Product.objects.filter(category = category)

    ctx = {
        'category' : category,
        'products' : products,
    }

    return render(request,"store/list-category.html",ctx)
     
