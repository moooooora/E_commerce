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
    

    class Meta:
        verbose_name = ("CartItem")
        verbose_name_plural = ("CartItems")

    def __str__(self):
        return str(self.product)

    # def get_absolute_url(self):
    #     return reverse("CartItem_detail", kwargs={"pk": self.pk})
    
