from django.contrib import admin
from .models import BusinessCard


@admin.register(BusinessCard)
class BusinessCardAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "company_name",
        "updated_at",
        "created_at",
    )
    date_hierarchy = "updated_at"
    list_filter = ("company_name", "updated_at", "created_at")
    ordering = ("full_name", "company_name", "-updated_at", "-created_at")

    search_fields = ("full_name", "company_name", "email", "phone_number")
    search_help_text = "Search by full name, company, email or phone number."

    readonly_fields = ("created_at", "updated_at")
    fieldsets = [
        (
            "Main",
            {
                "fields": (
                    ("full_name", "company_name"),
                    ("email", "phone_number"),
                    "slug",
                ),
                "description": "Business Card details",
            },
        ),
        (
            "Files",
            {
                "fields": ("image",),
                "description": "Business Card files",
                "classes": ("collapse",),
            },
        ),
        (
            "Info",
            {
                "fields": (
                    "owner",
                    ("created_at", "updated_at"),
                ),
                "description": "Technical information",
                "classes": ("collapse",),
            },
        ),
    ]

    list_per_page = 50
    # list_max_show_all = 500
