from django.db import models
from django.contrib.auth.models import User
from trform.models import Trform
# Create your models here.
class Packet(models.Model):
        user            = models.ForeignKey(User)
        trform = models.IntegerField(blank=True,null=True)
        deliver                 = models.CharField(max_length=50)
        deliver_no              = models.CharField(max_length=50)
        shopping_site   = models.CharField(max_length=50)
        content                 = models.CharField(max_length=50)
        status          = models.CharField(max_length=50)
        rep_no = models.CharField(max_length=50,blank=True,null=True)
        userdesc = models.CharField(max_length=50,blank=True,null=True)
        mgrdesc = models.CharField(max_length=50,blank=True,null=True)
        createtime              = models.DateTimeField()
        updatetime      = models.DateTimeField()	       