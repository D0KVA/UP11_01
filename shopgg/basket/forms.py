from django import forms
from shop.models import Order


class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(
        min_value=1,
        max_value=30,
        initial=1,
        label='Количество',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    reload = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_addresses',
            'delivery_type',
        )