from django.db import models
from django.utils.text import slugify
from category.models import Category


# Create your models here.
def image_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'{instance.product_name}.{extension}'
class Product(models.Model):

    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True,blank=True,null=True)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    stock = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,)
    modified_at = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def save(self,*args,**kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)  

    def __str__(self):
        return self.product_name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})
