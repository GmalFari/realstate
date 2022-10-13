# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import Realstate_com

class Realstate_com_Admin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = Realstate_com
    list_display = ['username', 'mobile_number','rs_com_name','rs_address']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number', 'rs_com_name','rs_address')}),
    ) #this will allow to change these fields in admin module


admin.site.register(Realstate_com, Realstate_com_Admin)
