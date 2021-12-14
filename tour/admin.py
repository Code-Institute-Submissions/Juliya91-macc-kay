from django.contrib import admin
from .models import Tour


class TourAdmin (admin.ModelAdmin):
    fields = ('first_name', 'last_name',
              'email', 'preferred_time',)


admin.site.register(Tour, TourAdmin)
