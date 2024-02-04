from django.db import models
from store.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    class Meta:
        verbose_name = ("CartItem")
        verbose_name_plural = ("CartItems")

    def __str__(self):
        return str(self.product)

    # def get_absolute_url(self):
    #     return reverse("CartItem_detail", kwargs={"pk": self.pk})
    
class Coupon(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    ratio = models.FloatField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupones")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Coupo_detail", kwargs={"pk": self.pk})
