from django.conf.urls import patterns, url

from poll import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
		       url(r'^(?P<id>\d+)/$',views.cat,name='cat'),
			)
