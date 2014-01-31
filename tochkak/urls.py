from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', include('newsfeed.urls')),
    url(r'^news/', include('newsfeed.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

### code to show images

if settings.DEBUG:
# static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^md/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}
            ))
