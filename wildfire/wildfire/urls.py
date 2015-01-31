from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wildfire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^access_all_tweets$', 'heatmap.views.access_all_tweets', name='access_all_tweets'),
    url(r'^$', 'heatmap.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
