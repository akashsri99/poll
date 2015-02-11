from django.conf.urls import patterns, url

from poll import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
		       url(r'^(?P<id>\d+)/$',views.cat,name='cat'),
		       url(r'^(?P<id>\d+)/detail/$',views.detail,name='detail'),

		       url(r'^submit/$',views.submit_form,name='submit_form'),
			)
