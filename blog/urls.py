from blog.views import PostLV
from django.conf.urls import url
urlpatterns = [
    # :8000/post
    url( r'^post/$', PostLV.as_view(), name='post_list' ),

]