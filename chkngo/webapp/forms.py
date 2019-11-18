from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ReviewForm(forms.ModelForm):
    Rating = forms.IntegerField(max_value=5, min_value= 0)
    class Meta:
        model = Review
        fields = ['Rating']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    contact = forms.CharField(required=False, max_length=11, min_length= 3)
    class Meta :
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'contact',
            'password1',
            'password2'
            ]
