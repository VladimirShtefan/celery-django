from django.contrib import admin

from coverter.models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'rate_to_usd', "updated_date", )
    exclude = ()
