from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urpoll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',RedirectView.as_view(url='http://upollet.com/home'),name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',include('poll.urls')),
    url(r'',include('social_auth.urls')),
    

)
