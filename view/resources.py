# myapp/api.py
from tastypie.resources import ModelResource
from rss.models import In
#from django.utils.html import strip_tags
import feedparser

class RssInRessource(ModelResource):
    class Meta:
        rss = "http://www.24ur.com/rss/"
        feed = feedparser.parse( rss )
        queryset = feed['items']
        for i in feed['items']:
            #qu = Q(strip_tags(i['summary']), i['title'], i['link'])
            queryset.extend(i)
        resource_name = 'rssin'