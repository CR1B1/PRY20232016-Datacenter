# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""
    model=User

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Extra info'), {'fields': ('role','dni', 'administrator', 'user_area', 'authorization', 'change_password', 'company_logo')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email','role')

admin.site.register(User, UserAdmin)