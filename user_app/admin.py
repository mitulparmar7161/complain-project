from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_app.models import *
from rest_framework.authtoken.admin import TokenProxy
from allauth.account.admin import EmailAddress
from django.contrib.auth.models import Group
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone', 'email', 'is_verified', 'user_type', 'date_joined')
    list_filter = ('is_verified', 'user_type')
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'otp')}),
        ('Permissions', {'fields': ('is_verified', 'user_type', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password1', 'password2', 'otp', 'user_type', 'is_verified', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('phone', 'email')
    ordering = ('phone', 'email')

# Register the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StaffUser)

admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)