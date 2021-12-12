from django.contrib import admin
from .models import Capture, Artist


class CaptureAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'price',
        'image',
    )

    ordering = ('sku',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'artist_statement',
    )


admin.site.register(Capture, CaptureAdmin)
admin.site.register(Artist, ArtistAdmin)
