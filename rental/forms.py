from django import forms
from .models import *


class HouseForm(forms.ModelForm):
    class Meta:
        model=House
        exclude=('user',)
        # fields=()