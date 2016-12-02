from tastypie.resources import ModelResource

from songs.models import Song


class SongResource(ModelResource):
    class Meta:
        fields = ['title', 'author', 'link']
        queryset = Song.objects.all().order_by('-created')
        resource_name = 'song'
        include_resource_uri = False