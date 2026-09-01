from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')
    search_fields = ('name',)
    list_filter = ('category',)

    def image(self, obj):
        if obj.img:
            return format_html(
                '{}',
                obj.img.url
            )
        return '画像なし'

    image.short_description = '画像'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)