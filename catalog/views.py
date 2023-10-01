from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Product


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Наш ассортимент'
    }


def contacts(request):
    return render(request, 'catalog/contacts.html')


class GoodsView(ListView):
    model = Product
    template_name = 'catalog/goods.html'
    extra_context = {
        'title': 'Наши товары'
    }


def category_stuff(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
    }
    return render(request, 'catalog/stuff.html', context)
