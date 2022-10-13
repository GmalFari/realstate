from django import forms

from .models import Realstate, RealstateImage


class RealstateForm(forms.ModelForm):
    class Meta:
        model= Realstate 
        fields = '__all__'
        exclude = ('company',)


class ImageRealstateForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple":True})
    )
    class Meta:
        model = RealstateImage
        fields = ("image",)
