from django import forms
from myapp.models import *

class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields = "__all__"