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
        session = form.cleaned_data.get('session')
        status = form.cleaned_data.get('status')
        age = form.cleaned_data.get('age')

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        if color:
            products = products.filter(color__iexact=color)

        if session:
            products = products.filter(session__iexact=session)

        if status:
            products = products.filter(status__iexact=status)

        if age:
            products = products.filter(age__iexact=age)


    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'product_list.html', context)
