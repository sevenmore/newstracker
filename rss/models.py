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


class Tags(models.Model):
    id_tag = models.AutoField(primary_key=True)
    tag_ltrack = models.CharField(max_length=20)
    tag_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag_name


class Feed(models.Model):
    id_feed = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    summary = models.CharField(max_length=400)
    published = models.DateTimeField('date published')
    tags_track = models.ManyToManyField(Tags)
    tags = models.CharField(max_length=400)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.title, self.published)


class Subscription(models.Model):
    id_sub = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    subs = models.ManyToManyField(Tags)

    def __unicode__(self):
        su = ""
        for i in self.subs.all():
            su = i.tag_name + ";" + su
        return u'{0}: {1}'.format(self.user, su)


