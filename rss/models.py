from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class In(models.Model):
    id_rss = models.AutoField(primary_key=True)
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=400)
    tags = models.CharField(max_length=400)

    def __unicode__(self):
        return self.url


class Out(models.Model):
    id_rss = models.AutoField(primary_key=True)
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.CharField(max_length=400)
    tags = models.CharField(max_length=400)


class Feed(models.Model):
    id_feed = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    published = models.CharField(max_length=400)

    def __unicode__(self):
        return self.published


class Subscription(models.Model):
    id_sub = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    subs = models.ForeignKey(Out)
