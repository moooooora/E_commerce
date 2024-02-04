from django.contrib import admin
from .models import Cart,CartItem,Coupon

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id','date_added']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    
    list_display = ['product','quantity','is_active']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['name','value','ratio','published_at','is_active']
    

