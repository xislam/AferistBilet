from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('inn_id', 'fio', 'gender', 'phone_number', 'email', 'status')
    list_display_links = ('inn_id', 'fio', 'phone_number', 'email')

    fieldsets = (
        (None, {'fields': ('inn_id', 'fio', 'gender', 'phone_number', 'email', 'status', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'inn_id', 'fio', 'gender', 'phone_number', 'email', 'status', 'password1', 'password2', 'is_staff',
            'is_active', 'is_superuser')}
         ),
    )
    search_fields = ('inn_id', 'fio', 'phone_number', 'email')
    ordering = ('fio',)


admin.site.register(User, CustomUserAdmin)
