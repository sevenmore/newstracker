from django.db import models

# Create your models here.


class RssIn(models.Model):
    id_rss = models.IntegerField(primary_key=True) 
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.charField(max_length=400)
	tags = models.charField(max_length=400)


class RssOut(models.Model):
    id_rss = models.IntegerField(primary_key=True) 
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    url = models.charField(max_length=400)
    tags = models.charField(max_length=400)
	
class Users(models.Model):
	id_user=models.IntegerField(primary_key=True) 
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=40)
	subscription = models.ManyToManyField(RssOut, through='Subscription')
	
class Subscription(models.Model):
    user = models.ForeignKey(Users)
    subs = models.ForeignKey(RssOut)
    
	