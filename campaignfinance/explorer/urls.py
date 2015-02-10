from django.conf.urls import patterns, url
from explorer import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^race/(?P<ward>\d+)/$', view=views.race, name='race'),
        url(r'^candidate/(?P<id>\d+)/$', view=views.candidate, name='candidate'),
)