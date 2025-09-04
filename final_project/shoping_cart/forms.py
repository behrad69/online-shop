from django import forms
from .models import cart

class cartform(forms.ModelForm):
    class Meta:
        model = cart
        fields = ['quantity', 'color']