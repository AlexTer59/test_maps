from django import forms
from .models import Search

class SearcForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['address', ]