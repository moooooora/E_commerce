from django.db import models
from django.utils.text import slugify

# Create your models here.
def image_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    
    return f'category/{instance.category_name}.{extension}'
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
    
    

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})
