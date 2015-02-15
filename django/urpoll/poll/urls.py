from django.conf.urls import patterns, url

from poll import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
		       url(r'^(?P<id>\d+)/$',views.cat,name='cat'),
		       url(r'^(?P<id>\d+)/detail/$',views.detail,name='detail'),

		       url(r'^(?P<id>\d+)/submit_form/$',views.submit_form,name='submit_form'),
		       url(r'^(?P<id>\d+)/reason_opt/$',views.reason_opt,name='reason_opt'),
		       url(r'^(?P<id>\d+)/get_comments/$',views.get_comments,name='get_comments'),
			)
