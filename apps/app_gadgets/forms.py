from django import forms
from .models import TechBox, Employee


class AddToolForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter Tool'}))
    class Meta:
        model = TechBox
        fields = ['name']