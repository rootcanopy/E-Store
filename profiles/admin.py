from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', ]


admin.site.register(User, CustomUserAdmin)
