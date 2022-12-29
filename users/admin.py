from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # user page 내 상세
    fieldsets = (
        (
            "Profile", 
            {
                "fields": ("username","password","name","email","is_host"),
                "classes":("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields" : (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important Dates",
            {
                "fields":(
                    "last_login",
                    "date_joined",
                ),
                "classes":(
                    "collapse",
                ),
            },
        ),
    )
    # user list 구성
    list_display = ("username","email","name","is_host")