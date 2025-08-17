from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CMSUser

class CMSUserAdmin(BaseUserAdmin):
    model = CMSUser
    list_display = ("phone_number", "role", "full_name", "date_of_birth", "is_active", "is_staff")
    search_fields = ("phone_number", "full_name")
    list_filter = ("role", "is_active", "is_staff")
    ordering = ("phone_number",)

admin.site.register(CMSUser, CMSUserAdmin)
