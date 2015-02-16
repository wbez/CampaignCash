from django.conf.urls import patterns, url
from explorer import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^race/(?P<slug>[-\w\d]+)/$', view=views.race, name='race'),
        url(r'^candidate/(?P<slug>[-\w\d]+)/$', view=views.candidate, name='candidate'),
        url(r'^candidate/(?P<slug>[-\w\d]+)/json/$', view=views.datatables, name='datatables'),
)