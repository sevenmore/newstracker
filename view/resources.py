# myapp/api.py
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from django.utils.html import strip_tags
import feedparser


class RssInRessource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'rssin'
