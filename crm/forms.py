from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    phone = forms.CharField(max_length=200)