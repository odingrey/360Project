from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^edit/', 'project.views.edit'),
    url(r'^delete/', 'project.views.delete_image'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/slowergram'}),
    url(r'^main', 'project.views.main'),
    url(r'^register/', 'project.views.register'), 
    url(r'^remove_account/', 'project.views.remove_account'),
    url(r'^settings', 'project.views.settings'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT}),
    url(r'^upload', 'project.views.upload_file'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
