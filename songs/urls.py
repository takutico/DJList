from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^2/$', views.index2, name='index2'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<song_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/vote/$', views.vote, name='vote'),
]