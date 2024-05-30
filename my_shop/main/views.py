from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product


def index(request):
    f = open('file.txt', 'r')

    return HttpResponse(f.read())


def products_list(request):
    products = Product.objects.all()
    template_name = "main/list.html"
    return render(request, template_name, context={"products": products})


def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        template_name = "main/details.html"
        return render(request, template_name, context={"item": product})
    except Product.DoesNotExist:
        raise Http404("Товар не найден")
