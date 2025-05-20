from django.contrib import admin

from .models import Graffiti


@admin.register(Graffiti)
class GraffitiAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at")
    search_fields = ("author__username",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    readonly_fields = ("author", "likes_count", "svg_preview", "created_at")
    fields = ("author", "likes_count", "svg_preview", "svg_data", "created_at")

    def svg_preview(self, obj):
        """
        Renders the SVG image in the admin detail view.
        """
        return obj.svg_data
