from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        db_table = 'custom_user'



    latitude_1 = models.DecimalField(max_digits = 9, decimal_places=6 ,blank = True,null = True)
    longitude_1 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)

    latitude_2 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)
    longitude_2 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)

    latitude_3 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)
    longitude_3 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)

    latitude_4 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)
    longitude_4 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)

    latitude_5 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)
    longitude_5 = models.DecimalField(max_digits = 9, decimal_places=6,blank = True,null = True)


class Content(models.Model):

    accounts = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    content = models.CharField(verbose_name ='content',max_length = 200)

    latitude = models.DecimalField(max_digits = 9, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)
