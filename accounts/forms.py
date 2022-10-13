from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Realstate_com



class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Realstate_com
        fields = ('username', 'mobile_number')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Realstate_com
        fields = ('username', 'mobile_number', 'rs_com_name','rs_address')

class UserForm(forms.ModelForm):
    class Meta:
        model = Realstate_com
        fields = ['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image','address']