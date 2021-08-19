from django.contrib import admin
from .models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'allergens',
        'price',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
