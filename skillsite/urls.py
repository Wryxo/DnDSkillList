from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'skillsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ff/', include('ff.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('skilllist.urls')),
]
