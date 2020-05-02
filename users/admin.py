from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, WorksAt

admin.site.register(WorksAt)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('id', 'first_name', 'last_name', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'email', 'password1', 'password2', 'mobile'),
        }),
    )
    list_display = ('id', 'email', 'first_name', 'last_name', 'mobile', 'is_staff')
    search_fields = ('id', 'email', 'first_name', 'last_name', 'mobile')
    ordering = ('id',)
