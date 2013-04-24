# myapp/api.py
from tastypie.resources import ModelResource
from rss.models import In


class RssInRessource(ModelResource):
    class Meta:
        queryset = In.objects.all()
        resource_name = 'rssin'
