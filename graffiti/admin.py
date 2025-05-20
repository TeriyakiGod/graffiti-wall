from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Graffiti


@admin.register(Graffiti)
class GraffitiAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at")
    search_fields = ("author__username",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    readonly_fields = ("author", "likes_count", "likes", "svg_preview", "created_at")
    fields = ("author", "likes_count", "likes", "svg_preview", "svg_data", "created_at")

    def svg_preview(self, obj):
        """
        Renders the SVG image in the admin detail view.
        """
        return mark_safe(obj.svg_data)  # noqa: S308
