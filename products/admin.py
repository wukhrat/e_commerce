from django.contrib import admin
from products.models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_display = ('title', 'description', 'price')


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Category, CategoryAdmin)
