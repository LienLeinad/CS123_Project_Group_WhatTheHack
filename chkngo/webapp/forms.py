from django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    Rating = forms.IntegerField(max_value=5, min_value= 0)
    class Meta:
        model = Review
        fields = ['Rating']