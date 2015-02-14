from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'campaignfinance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^elections/staging/', include('explorer.urls')),
)

urlpatterns += staticfiles_urlpatterns()
