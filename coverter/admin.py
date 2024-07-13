from django.contrib import admin

from coverter.models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    exclude = ()
