from django.shortcuts import render
from .models import Product
from .forms import ProductFilterForm


def product_list(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        color = form.cleaned_data.get('color')

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        if color:
            products = products.filter(color__iexact=color)

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'product_list.html', context)
