# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from rss.models import Feed
from django.utils.html import strip_tags
import feedparser


class RssInRessource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()
        filtering = {
            'tags': ALL,
            }
        resource_name = 'rssin'
