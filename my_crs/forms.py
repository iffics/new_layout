from django import forms
from django.contrib.auth.models import User
from.models import Shops,Reviews
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ['username', 'email','password']






class ShopsForm(forms.ModelForm):

    class Meta:
        model = Shops
        fields = ['name','address','cellnum','image',]




class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['product_name','shop_name','comment_title','comment','product_image']