from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff',)
    list_filter = ('username', 'is_staff',)
    fieldsets = ((None, {'fields': ('username', 'password')}), ('Permissions', {'fields': ('is_staff',)}),)
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2', 'is_staff',)}),)
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
