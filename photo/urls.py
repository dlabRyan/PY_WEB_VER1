from django.conf.urls import url
from photo.views import *

urlpatterns = [

    # Example: /
    url(r'^$', AlbumLV.as_view(), name='index'),

    #E Example: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail' ),

]