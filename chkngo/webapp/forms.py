from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ReviewForm(forms.ModelForm):
    Rating = forms.IntegerField(max_value=5, min_value= 0)
    ReviewDetail = forms.CharField(max_length = 250, label = 'Review')
    class Meta:
        model = Review
        fields = ['Rating','ReviewDetail']

class RegistrationForm(UserCreationForm):
    CUSTOMER = "CU"
    RESTAURANT_MANAGER = "RM"
    USER_TYPES = [
        (CUSTOMER,'Customer'),
        (RESTAURANT_MANAGER,'Restaurant Manager'),
    ]
    user_type = forms.ChoiceField(choices = USER_TYPES)
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    contact = forms.CharField(required=False, max_length=11, min_length= 3)
    class Meta :
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'user_type',
            'username',
            'email',
            'contact',
            'password1',
            'password2'
            ]

class RMRegistrationForm(forms.ModelForm):
    RestoID = forms.CharField(max_length= 30, required = False, label = "Restaurant ID")
    Category = forms.ModelMultipleChoiceField(queryset = Categories.objects.all(), required = False)
    class Meta:
        model = Restaurant
        fields= ['RestoID',]


class CategoryForm(forms.ModelForm):
    CatName = forms.CharField(max_length = 30, label = 'Category Name')
    class Meta:
        model = Categories
        fields = ['CatName']