from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Trform(models.Model):
        user            = models.ForeignKey(User)
        fee  = models.IntegerField()
        weight = models.IntegerField()
        userdesc                = models.CharField(max_length=50)
        mgrdesc         = models.CharField(max_length=50)
        createtime              = models.DateTimeField()
        updatetime      = models.DateTimeField()	