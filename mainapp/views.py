from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import Product, Category
from mainapp.services import get_basket, get_hot_product, get_same_products


def index(request):
    context = {
        'products': Product.objects.all()[:4],
    }
    return render(request, "mainapp/index.html", context)


def products(request, pk=None):
    links_menu = Category.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all().order_by('price')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(Category, pk=pk)
            products_list = Product.objects.filter(category_id=pk)

        page = request.GET.get('page')
        paginator = Paginator(products_list, 2)
        try:
            paginator_products = paginator.page(page)
        except PageNotAnInteger:
            paginator_products = paginator.page(1)
        except EmptyPage:
            paginator_products = paginator.page(paginator.num_pages)

        context = {
            'links_menu': links_menu,
            'products': paginator_products,
            'category': category_item,
        }

        return render(request, 'mainapp/products_list.html', context)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'links_menu': Category.objects.all(),
        'product': product_item,
    }
    return render(request, 'mainapp/product.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')
