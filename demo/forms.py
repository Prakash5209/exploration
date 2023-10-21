from django import forms

from demo.models import DemoModel

class DemoModelForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))