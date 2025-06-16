from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'zip_code',]
        widgets = {
            'street': forms.TextInput(attrs={'placeholder': '123 Main St'}),
            'city': forms.TextInput(attrs={'placeholder': 'Springfield'}),
            'state': forms.TextInput(attrs={'placeholder': 'CA'}),
            'zip_code': forms.TextInput(attrs={'placeholder': '90210'}),
        }