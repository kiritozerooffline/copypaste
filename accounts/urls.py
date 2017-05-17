from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
