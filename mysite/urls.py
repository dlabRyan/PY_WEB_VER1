"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import HomeView, BookmarkView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'blog/', include('blog.urls', namespace='blog')),

    url(r'^photo/', include('photo.urls', namespace='photo')), #추가

    url(r'^bookmark/$', BookmarkLV.as_view(),
        name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(),
        name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) #추가
