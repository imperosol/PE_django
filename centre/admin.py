from django.contrib import admin
from .models import Centre
from stock.models import Stock


class StockInline(admin.StackedInline):
    model = Stock
    extra = 1


class CentreAdmin(admin.ModelAdmin):
    inlines = [StockInline]


admin.site.register(Centre, CentreAdmin)
