from django.conf.urls import patterns, url

from poll import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
		       url(r'^(?P<id>\d+)/$',views.cat,name='cat'),
		       url(r'^(?P<id>\d+)/detail/$',views.detail,name='detail'),

		       url(r'^(?P<id>\d+)/submit_form/$',views.submit_form,name='submit_form'),
		       url(r'^(?P<id>\d+)/reason_opt/$',views.reason_opt,name='reason_opt'),
		       url(r'^(?P<id>\d+)/get_comments_A/$',views.get_comments_A,name='get_comments_A'),
		       url(r'^(?P<id>\d+)/get_comments_B/$',views.get_comments_B,name='get_comments_B'),
		       url(r'^(?P<id>\d+)/get_comments_C/$',views.get_comments_C,name='get_comments_C'),
		       url(r'^(?P<id>\d+)/get_comments_D/$',views.get_comments_D,name='get_comments_D'),
		       url(r'^(?P<id>\d+)/detail/submit_question$',views.submit_question,name='submit_question'),
		       
		       
		       

			)
