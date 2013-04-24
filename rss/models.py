from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class In(models.Model):
    id_rss = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=400)
    tags = models.CharField(max_length=400)

    def __unicode__(self):
        return self.url


class Out(models.Model):
    id_rss = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=400)
    tags = models.CharField(max_length=400)

#class Users(models.Model):
    #id_user=models.IntegerField(primary_key=True)
    #username=models.CharField(max_length=20)
#    subscription = models.ManyToManyField(RssOut, through='Subscription')


class Subscription(models.Model):
    user = models.ForeignKey(User)
    subs = models.ForeignKey(Out)
