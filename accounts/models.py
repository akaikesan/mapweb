from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        db_table = 'custom_user'

    email = models.EmailField(null = False, unique=True,blank = False)

    image = models.ImageField(upload_to='images/', null=True, blank = True)



    self_introduce = models.CharField(verbose_name ='self_introduce',max_length = 500,null=True,blank=True)

    def get_followers(self):
        relations = Relationship.objects.filter(follow=self)
        return [relation.follower for relation in relations]


class RelationShip(models.Model):

    follow = models.ForeignKey(CustomUser, related_name='follows',on_delete=models.CASCADE)
    follower = models.ForeignKey(CustomUser, related_name='followers',on_delete=models.CASCADE)


class Content(models.Model):

    #if CustomUser is deleted, this Content will be deleted.
    accounts = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    fav = models.IntegerField(verbose_name = 'favorite', default=0)

    content = models.CharField(verbose_name ='content',max_length = 200)

    date = models.DateTimeField(default = timezone.now)

    latitude = models.DecimalField(max_digits = 9, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)

    image = models.ImageField(upload_to='images/', null=True)
