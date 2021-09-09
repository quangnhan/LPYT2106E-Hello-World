from django.http import HttpResponse
from django.shortcuts import render
from untils.mock_api import MockApi


def product(request):
    id = request.GET.get("id")
    mock_api = MockApi()
    products = mock_api.get_products_by_category(id)

    data = {"category": "Clothes", "my_products": products}
    return render(request, 'pages/product.html', data)


def category(request):
    return render(request, 'pages/category.html')
