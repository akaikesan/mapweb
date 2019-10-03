from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        db_table = 'custom_user'

    image = models.ImageField(upload_to='images/' ,null=True)

    self_introduce = models.CharField(verbose_name ='self_introduce',max_length = 500,null=True,blank=True)






class Content(models.Model):

    #if CustomUser is deleted, this Content will be deleted.
    accounts = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    fav = models.IntegerField(verbose_name = 'favorite', default=0)

    content = models.CharField(verbose_name ='content',max_length = 200)

    date = models.DateTimeField(default = timezone.now)

    latitude = models.DecimalField(max_digits = 9, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)

    image = models.ImageField(upload_to='images/' ,null=True)
