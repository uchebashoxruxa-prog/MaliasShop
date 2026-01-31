from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ModelProduct)
admin.site.register(ImagesProduct)
admin.site.register(Customer)
admin.site.register(FavouriteProduct)
admin.site.register(Cart)
admin.site.register(ProductCart)
admin.site.register(Delivery)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(Contact)
admin.site.register(DeliveryMethod)
admin.site.register(PaymentMethod)
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category_item')
    list_display_links = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',)}

    def category_item(self, obj):
        if obj.icon:
            try:
                return mark_safe(f'<img src="{obj.icon.url}" width="30" >')
            except:
                return 'No icon'
        else:
            return 'No icon'


@admin.register(ModelProduct)
class ModelProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',)}


class ImagesProductInline(admin.TabularInline):
    model = ImagesProduct
    fk_name = 'product'
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'quantity', 'discount', 'category', 'model', 'product_image')
    list_display_links = ('pk', 'title', 'category', 'model')
    prepopulated_fields = {'slug': ('title', )}
    inlines = [ImagesProductInline]
    list_editable = ('price', 'quantity', 'discount')
    list_filter = ('price', 'discount', 'category', 'model')

    def product_image(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.first().image.url}" width="70">')
            except:
                return 'No photo'
        else:
            return 'No photo'
