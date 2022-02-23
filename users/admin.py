from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, ShippingAddress

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("email", "username", "password")}
        ),
        (
            _("Timelines"),
            {"fields": ("last_login", "date_joined")}
        ),
        (
            _("Permissions"),
            {"fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )},
        ),
    )

    list_display = ("email", "is_staff")


@admin.register(ShippingAddress)
class CustomShippingAddressAdmin(admin.ModelAdmin):
    pass

# @admin.register(UserFavorite)
# class CustomFavouriteAdmin(admin.ModelAdmin):
#     pass
