from django.shortcuts import render


def index(reqests):
    return render(reqests, 'mainapp/index.html')


def products(reqests):
    return render(reqests, 'mainapp/products.html')


def contact(reqests):
    return render(reqests, 'mainapp/contact.html')
