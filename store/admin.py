from django.contrib import admin
from .models import Product,Offer
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','category','stock','created_at','modified_at','is_available']
    
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['product','ratio','is_active']

    list_editable = ['is_active',]


