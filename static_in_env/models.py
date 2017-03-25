from audioop import reverse

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings

class Shops(models.Model):

    image = models.FileField(null=True,blank=True)
    name = models.CharField(max_length=33)
    address = models.CharField(max_length=33)
    cellnum = models.CharField(max_length=33)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)


    def __str__(self):
        return self.name



class Reviews(models.Model):

    product_name = models.CharField(max_length=30)
    shop_name = models.ForeignKey(Shops)
    comment_title = models.CharField(max_length=30)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    product_image = models.FileField(null=True, blank=True)
    r_user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)


    def __str__(self):
        return "%s %s" % (self.product_name, self.comment_title)



