from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def profile_upload(instance,filename:str):
    extension = filename.split('.')[1]
    return f'accounts/{instance.user}.{extension}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=profile_upload, height_field=None, width_field=None, max_length=None)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)

