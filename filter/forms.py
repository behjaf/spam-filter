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

    session_choices = [
        ('', 'Select session'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ]
    session = forms.ChoiceField(label='session', choices=session_choices, required=False)

    status_choices = [
        ('', 'Select availability'),
        ('true', 'True'),
        ('false', 'False'),
    ]
    status = forms.ChoiceField(label='status', choices=status_choices, required=False)

    age_choices = [
        ('', 'Select age'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('child', 'Child'),
        ('Baby', 'baby'),
    ]
    age = forms.ChoiceField(label='age', choices=age_choices, required=False)