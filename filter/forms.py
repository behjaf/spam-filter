# forms.py

from django import forms
from .models import Product


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)
    color_choices = [
        ('', 'Select Color'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('brown', 'Brown'),
    ]
    color = forms.ChoiceField(label='Color', choices=color_choices, required=False)
