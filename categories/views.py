from unicodedata import name
from django.core.paginator import Paginator

from django.shortcuts import render, redirect

from products.models import Category, Product
from django.views import View


class CategoryDetailView(View):
    def get(self, request):
        category = Category.objects.get(name="kabel")
        print(category.name)
        return render(request, "categories/detail.html",
                      {"category": category})  # bu qolda yozilgan tepadagi esa generic view bilan


class CategoryCableView(View):
    def get(self, request):
        products = Product.objects.filter(category_id=1)
        search_query = request.GET.get("q", "")
        if search_query:
            products = products.filter(title__icontains=search_query)
        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(products, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        category = Category.objects.get(name='kabel')
        return render(request, "categories/cables.html",
                      {"page_obj": page_obj, "category": category})


class CategoryElectricalView(View):
    def get(self, request):
        products = Product.objects.filter(category_id=3)
        search_query = request.GET.get("q", "")
        if search_query:
            products = products.filter(title__icontains=search_query)
        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(products, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        category = Category.objects.get(name='kabel')
        return render(request, "categories/electrical.html",
                      {"page_obj": page_obj, "category": category})



class CategoryRozetkiView(View):
    def get(self, request):
        products = Product.objects.filter(category_id=4)
        search_query = request.GET.get("q", "")
        if search_query:
            products = products.filter(title__icontains=search_query)
        page_size = request.GET.get("page_size", 4)
        paginator = Paginator(products, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        category = Category.objects.get(name='kabel')
        return render(request, "categories/rozetki.html",
                      {"page_obj": page_obj, "category": category})