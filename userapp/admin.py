from atexit import register
from django.contrib import admin
from .models import (Banner, Brand, Color, Customers, Orders, catagory,giftcard,seo,Product,Tags,metadata,
ProductImage,giftcard,Product_type, Slider,Color,Size,Variants,Events)
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.site_header = "Ecommerce Main Admin"
admin.site.site_title = "Admin Ecommerce"
admin.site.index_title = "Ecommerce"

admin.site.register(catagory)
admin.site.register(Brand)
admin.site.register(Product_type)
admin.site.register(giftcard)
admin.site.register(ProductImage)
admin.site.register(metadata)
@admin.register(Product)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(seo)
admin.site.register(Slider)
admin.site.register(Tags)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variants)
admin.site.register(Orders)
admin.site.register(Customers)
admin.site.register(Events)
admin.site.register(Banner)


