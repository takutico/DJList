from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from songs.models import Song


class SongResource(ModelResource):
    class Meta:
        fields = ['created', 'title', 'author', 'link']
        queryset = Song.objects.all().order_by('-created')
        resource_name = 'song'
        include_resource_uri = False
        authorization = Authorization()
        always_return_data = True
